# Retorna uma string com # no início, no meio e no final 
# str-> str
def hashtag(s):
    metade=len(s)//2
    return '#'+s[0:metade]+'#'+s[metade:]+'#'