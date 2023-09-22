# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    x=len(s)//2
    hashtageado = '#'+s[0:x]+'#' + s[x:] + '#'
    return hashtageado