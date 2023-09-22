# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    x=len(s)
    y=x//2
    resposta='#'+[0:y]+'#'+[y:]+'#'
    return resposta