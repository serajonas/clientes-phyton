# View - o que vai para o usuário
def view():
    usuario_digitado = input("Informe o seu usuário: ")
    senha_digitado = input("Informe sua senha: ")
    controller(usuario_digitado,senha_digitado)