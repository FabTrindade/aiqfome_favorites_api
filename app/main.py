from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from dotenv import load_dotenv
load_dotenv()
from .database import SessionLocal, engine, Base
from . import models, schemas, crud, auth

Base.metadata.create_all(bind=engine)

app = FastAPI(title="aiqfome Favorites API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CRUD Clientes
@app.post("/clients/", dependencies=[Depends(auth.validate_token)])
def create_client(client: schemas.ClientCreate, db: Session = Depends(get_db)):
    return crud.create_client(db, client)

@app.get("/clients/{client_id}", dependencies=[Depends(auth.validate_token)])
def get_client(client_id: int, db: Session = Depends(get_db)):
    client = crud.get_client(db, client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return   client

@app.put("/clients/{client_id}", dependencies=[Depends(auth.validate_token)])
def update_client(client_id: int, update: schemas.ClientUpdate, db: Session = Depends(get_db)):
    return crud.update_client(db, client_id, update)

@app.delete("/clients/{client_id}", dependencies=[Depends(auth.validate_token)])
def delete_client(client_id: int, db: Session = Depends(get_db)):
    crud.delete_client(db, client_id)
    return {"detail": "Client deleted"}

# Favoritos
@app.post("/clients/{client_id}/favorites/", dependencies=[Depends(auth.validate_token)])
def add_favorite(client_id: int, favorite: schemas.FavoriteCreate, db: Session = Depends(get_db)):
    return crud.add_favorite(db, client_id, favorite)

@app.get("/clients/{client_id}/favorites/", dependencies=[Depends(auth.validate_token)])
def list_favorites(client_id: int, db: Session = Depends(get_db)):
    return crud.list_favorites(db, client_id)
