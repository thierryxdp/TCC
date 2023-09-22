#
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):def hashtag(string):
    """It returns the chosen string with one # on its left, one on its right, another one in its middle or in middle's left"""
    s=string
    n=len(s)
    b=int(break_index(n))
    if n%2==0:
        return '#'+s[:b]+'#'+s[b:]+'#'
    elif not n%2==0:
        return '#'+ s[:b]+'#'+s[b:]+'#'
def break_index(n):
	if n%2==0:
		return(n/2)
	elif not n%2==0:
		return((n-1)/2)