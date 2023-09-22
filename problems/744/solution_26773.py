# Coloque um comentário dizendo o que a função faz
# str-> str
def hashtag(s):
    i = len(s)//2
    return '#'+s[0:i]+'#'+s[i:]+'#'