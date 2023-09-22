#str-->str
#dado uma frase retorna essa frase ao contrário sem pontuações ou letras maiúsculas
def sep(a):
	import string
	z = string.punctuation
    for x in z:
    	a = a.replace(x,' ')
    return a
def inverte(c):
	import string
	g=sep(c)
	j=str.lower(g)
	k = j.split()
	h=reversed(k)
	l=" ".join(h)
	return l