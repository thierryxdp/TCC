# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(string):
    x=len(string)
    a=int(x/2)
    b="#"
    return b+string[0:a]+b+string[a:]