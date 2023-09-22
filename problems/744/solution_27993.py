# retorna a string dada com hashtang no inicio, meio e final
# str-> str
def hashtag(s):
    n=len(s)
    t=round (n/2-1)
    return '#'+s[:t]+'#'+s[t:]+'#'