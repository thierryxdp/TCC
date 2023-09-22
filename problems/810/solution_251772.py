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
	l=" ".join(k)
	return l