# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    S=len(str(s))
    return '#'+ str(s)[:S]+'#'+ str(s)[S:]+'#'