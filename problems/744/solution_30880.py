# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    t = len(s)
    y = t//2
    return '#'+s[0:y+1]+'#'+s[y+1:]+'#'