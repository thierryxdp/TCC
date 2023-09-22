# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    lim = len(s)
    return '#'+s[0:s/2]+'#'+[s/2:]+'#'