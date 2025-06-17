from fastapi import Header, HTTPException
import os

# Busca o token do ambiente e dá erro se não existir
API_TOKEN = os.getenv('API_TOKEN')
if API_TOKEN is None:
    raise RuntimeError("API_TOKEN não definido nas variáveis de ambiente.")

def validate_token(authorization: str = Header(...)):
    expected = f"Bearer {API_TOKEN}"
    if authorization != expected:
        raise HTTPException(status_code=401, detail="Invalid or missing token")
