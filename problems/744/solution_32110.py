# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    #Z=len(str(s))* 1/2#
    return '#'+ str(s)[:len(str(s)):2]+'#'+ str(s)[len(str(s)):]+'#'