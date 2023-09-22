# retorna a string dada com hashtang no inicio, meio e final
# str-> str
def hashtag(s):
    n=len(s) 
    k=n%2
    t=int(n/2)
    p=int((n-1)/2)
    
    if k==0:
 		return '#'+s[:t]+'#'+s[t:]+'#'
    else:
    	return '#'+s[:(p)]+'#'+s[(p):]+'#'