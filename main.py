# View - o que vai para o usuário
def view():
    usuario_digitado = input("Informe o seu usuário: ")
    senha_digitado = input("Informe sua senha: ")

# Model - O que vem do banco de dados (BD)
def model():
    usuario_BD = 'joao'
    senha_BD = '123'

# Controller - a validação
def controller():
    if usuario_digitado == usuario_BD and senha_digitado == senha_BD:
        print("pode entrar")
    else:
        print("usuário ou senha inválido")