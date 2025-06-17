from sqlalchemy.orm import Session
from fastapi import HTTPException
from . import models, schemas, external_api

def create_client(db: Session, client: schemas.ClientCreate):
    existing = db.query(models.Client).filter(models.Client.email == client.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    db_client = models.Client(name=client.name, email=client.email)
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

def get_client(db: Session, client_id: int):
    return db.query(models.Client).filter(models.Client.id == client_id).first()

def update_client(db: Session, client_id: int, update: schemas.ClientUpdate):
    db_client = get_client(db, client_id)
    if not db_client:
        raise HTTPException(status_code=404, detail="Client not found")

    if update.name:
        db_client.name = update.name
    if update.email:
        # TODO: validar se o novo email já existe
        db_client.email = update.email

    db.commit()
    db.refresh(db_client)
    return db_client

def delete_client(db: Session, client_id: int):
    db_client = get_client(db, client_id)
    if not db_client:
        raise HTTPException(status_code=404, detail="Client not found")
    db.delete(db_client)
    db.commit()

def add_favorite(db: Session, client_id: int, favorite: schemas.FavoriteCreate):
    product = external_api.get_product_by_id(favorite.product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found in external API")

    existing = db.query(models.Favorite).filter_by(client_id=client_id, product_id=favorite.product_id).first()
    if existing:
        raise HTTPException(status_code=400, detail="Product already in favorites")

    db_favorite = models.Favorite(client_id=client_id, product_id=favorite.product_id)
    db.add(db_favorite)
    db.commit()
    db.refresh(db_favorite)
    return db_favorite

def list_favorites(db: Session, client_id: int):
    favorites = db.query(models.Favorite).filter_by(client_id=client_id).all()
    products = []
    for fav in favorites:
        product = external_api.get_product_by_id(fav.product_id)
        if product:
            products.append({
                "id": product["id"],
                "title": product["title"],
                "image": product["image"],
                "price": product["price"],
                "review": product.get("rating", {}).get("rate")
            })
    return products
