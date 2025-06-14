from sqlalchemy import Column, Integer, String, Boolean, Text, DateTime
from datetime import datetime
from .database import Base

class Convidado(Base):
    __tablename__ = "convidados"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    confirmado = Column(Boolean, default=False)
    acompanhantes = Column(Integer, default=0)

class ChatLog(Base):
    __tablename__ = "chatlogs"
    id = Column(Integer, primary_key=True, index=True)
    pergunta = Column(Text, nullable=False)
    resposta = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    convidado_email = Column(String, nullable=True)
    
# backend/models.py (no final do arquivo)
if __name__ == "__main__":
    from .database import engine
    Base.metadata.create_all(bind=engine)
