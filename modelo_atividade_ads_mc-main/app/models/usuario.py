# app/models/usuario.py

class Usuario:
    def __init__(self, id_usuario: int, nome: str, senha: str):
    
        self._id = id_usuario
        self._nome = nome
        self._senha = senha

    def obter_permissoes(self):
        
        return []

class Visitante(Usuario):
    def obter_permissoes(self):
        return ["visualizar_produtos"]

class Contribuidor(Usuario):
    def obter_permissoes(self):
        return ["visualizar_produtos", "adicionar_produtos"]

class Moderador(Usuario):
    def obter_permissoes(self):
        return ["visualizar_produtos", "adicionar_produtos", "deletar_produtos", "gerenciar_usuarios"]