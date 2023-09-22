# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    nome = len(s)
    media = nome//2
    
    return '#' + s [ :media] +'#' + s[media: ] + '#'