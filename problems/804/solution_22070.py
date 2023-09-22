def par(n):
    return n%2==0

r = ()
def fitra_pares(t):
    if par(t[0]):
        r = r + (t[0],)
    if par(t[1]):
        r = r + (t[1],)
    if par(t[2]):
        r = r + (t[2],)
    if par(t[3]):
        r = r + (t[3],)
    else:
        r = r
	return r