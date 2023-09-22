def retira_pontuacao(a):
	import string
	z = string.punctuation
    for x in z:
    	a = a.replace(x,'')
    return(a)
def lower(b):
	return string.lower(b)