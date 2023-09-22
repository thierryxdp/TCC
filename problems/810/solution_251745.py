def b(a):
	import string
	z = string.punctuation
    for x in z:
    	a = a.replace(x,'')
    return string.lower(a)
def inverte(c):
	j=""
	y=c.split(" ")
    for h in y:
    	j += h[::-1]+" "
	return j