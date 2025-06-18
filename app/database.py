from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = os.getenv('DATABASE_URL')

if not DATABASE_URL:
    raise EnvironmentError("A variável de ambiente DATABASE_URL não está definida. Por favor, configure no seu .env ou no ambiente.")

# Criação do engine com pool de conexões
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

# Configuração da sessão
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos ORM
Base = declarative_base()
