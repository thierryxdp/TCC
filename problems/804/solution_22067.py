def par(n):
    return n%2==0

def fitro(t):
    r = ()
    if par(t[0]):
        r = r+ (t[0],)
    if par(t[1]):
        r = r+ (t[1],)
    if par(t[2]):
        r = r+ (t[2],)
    if par(t[3]):
        r = r+ (t[3],)
	return r