# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    listas = list(s)
    x=(listas//2)
    listas.extend('#')
    return listas