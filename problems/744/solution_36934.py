# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    l=len(s)
    a='#'+(s[:(l//2)])+'#'+(s[(l//2):])+'#'
    return a