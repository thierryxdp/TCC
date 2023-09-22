# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    y=len(s)//2
    x=str(s)
    return '#'+(str(s)[1:y])+'#'