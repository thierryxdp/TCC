def sep(a):
	import string
	z = string.punctuation
    for x in z:
    	a = a.replace(x,'')
    return a
def inverte(c):
	c=sep(c)
	c=string.lower(c)
	return y