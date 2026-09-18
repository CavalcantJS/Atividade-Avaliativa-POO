from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.controllers.auth_controller import autenticar_usuario

router = APIRouter(prefix="/auth", tags=["Autenticação"])


class Credenciais(BaseModel):
    nome: str
    senha: str

@router.post("/login")
def login(credenciais: Credenciais):
    resultado = autenticar_usuario(credenciais.nome, credenciais.senha)
    
    if resultado is None:
        raise HTTPException(status_code=401, detail="Usuário ou senha inválidos")
        
    return resultado