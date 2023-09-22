# retorna a string dada com hashtang no inicio, meio e final
# str-> str
def hashtag(s):
    n=len(s) 
    k=n%2
    t=float(n/2)
    if k==0:
 		return '#'+s[:t]+'#'+s[t:]+'#'
    else:
    	return '#'+s[:(t-1)]+'#'+s[(t-1):]+'#'