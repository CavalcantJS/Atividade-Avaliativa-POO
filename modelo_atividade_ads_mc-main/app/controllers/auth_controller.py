from app.data.usuarios_mock import USUARIOS
from app.models.usuario import Visitante, Contribuidor, Moderador


PERFIS = {
    'visitante': Visitante,
    'contribuidor': Contribuidor,
    'moderador': Moderador
}

def autenticar_usuario(nome_informado: str, senha_informada: str):
    for u in USUARIOS:
        if u['nome'] == nome_informado and u['senha'] == senha_informada:
           
            ClasseUsuario = PERFIS[u['perfil']]
            
            
            usuario_obj = ClasseUsuario(u['id'], u['nome'], u['senha'])
            
            
            return {
                "mensagem": f"Bem-vindo, {u['nome']}!",
                "permissoes_concedidas": usuario_obj.obter_permissoes()
            }
            
    return None