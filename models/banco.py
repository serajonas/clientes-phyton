# Model - O que vem do banco de dados (BD)
def model_usuario():
    arquivo = open("models\\dados.txt","r+")
    conteudo = arquivo.readlines()
    for linha in conteudo:
        usuario_senha = linha.split(";")
    usuario_BD = usuario_senha[0]
    return usuario_BD

def model_senha():
    senha_BD = '123'
    return senha_BD

print(model_usuario())