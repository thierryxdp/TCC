# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    n = len(s)//2
    t = '#'+s[:n]+'#'+s[n:]+'#'
    return t