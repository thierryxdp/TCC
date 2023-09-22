def sep(a):
	import string
	z = string.punctuation
    for x in z:
    	a = a.replace(x,'')
    return string.lower(a)
def inverte(c):
	c=sep(c)
	return y