# retorna a string dada com hashtang no inicio, meio e final
# str-> str
def hashtag(s):
    n=len(s)
    t=round (n/2)
    if t=int:
    	return '#'+s[:t]+'#'+s[t:]+'#'
    else:
    	return '#'+s[:(t-1)]+'#'+s[(t-1):]+'#'