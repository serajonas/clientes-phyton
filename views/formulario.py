import controllers.controllerAplicacao as controllerAplicacao
# View - o que vai para o usuário
def formulario_login():
    usuario_digitado = input("Informe o seu usuário: ")
    senha_digitado = input("Informe sua senha: ")
    controllerAplicacao.validar_login(usuario_digitado,senha_digitado)