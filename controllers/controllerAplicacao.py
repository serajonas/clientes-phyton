import models.banco as banco
import views.formulario as view

# Controller - a validação
def validar_login(usuario_completo):
    usuario_BD = banco.model_usuario()
    senha_BD = banco.model_senha()

    if usuario_completo[0] == usuario_BD and usuario_completo[1] == senha_BD:
        print("*** Pode entrar ***")
    else:
        print("*** Usuário ou senha inválido ***")

def iniciar():
    #usuario_completo = view.formulario_login()
    validar_login(view.formulario_login())        