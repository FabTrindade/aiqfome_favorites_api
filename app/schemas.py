from pydantic import BaseModel, EmailStr
from typing import List, Optional

# Schemas para Cliente

class ClientCreate(BaseModel):
    name: str
    email: EmailStr

class ClientUpdate(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]

# Schemas para Favorito

class FavoriteCreate(BaseModel):
    product_id: int

class FavoriteOut(BaseModel):
    id: int
    product_id: int

    class Config:
        orm_mode = True

class FavoriteProduct(BaseModel):
    id: int
    title: str
    image: str
    price: float
    review: Optional[str] = None

    class Config:
        orm_mode = True

# Schema de saída completo de Cliente, incluindo seus favoritos
class ClientOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    favorites: List[FavoriteOut] = []

    class Config:
        orm_mode = True
