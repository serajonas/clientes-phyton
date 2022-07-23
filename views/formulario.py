import controllers.validacao as validacao
# View - o que vai para o usuário
def formulario_login():
    usuario_digitado = input("Informe o seu usuário: ")
    senha_digitado = input("Informe sua senha: ")
    validacao.validar_login(usuario_digitado,senha_digitado)