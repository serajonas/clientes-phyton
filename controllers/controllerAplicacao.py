import models.banco as banco
import views.formulario as view

# Controller - a validação
def validar_login(usuario_completo):

    usuario_BD = banco.model_usuario()
    senha_BD = banco.model_senha()

    if usuario_completo[0] == usuario_BD and usuario_completo[1] == senha_BD:
        view.exibir_mensagem("*** Pode entrar ***")
        opcoes_menu()
    else:
        view.exibir_mensagem("*** Usuário ou senha inválido ***")

def iniciar():
    #usuario_completo = view.formulario_login()
    validar_login(view.formulario_login())   

def opcoes_menu():
    opcao = view.menu()
    if opcao == '1':
        print("Cadastro de Clientes")
    elif opcao == '2':
        print("Listagem de Clientes")
    else:
        view.exibir_mensagem("Sistema Finalizado")
        exit()

def cadastrar_cliente():
    cliente = view.cadastrar_cliente()
    banco.model_cadastro_cliente(cliente)              