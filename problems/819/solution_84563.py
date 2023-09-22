def filtra(ls, p):
	r = []
    for e in ls:
        if p(e):
            r.append(e)
	return r

def multiplo(n, q):
    if n%q==0:
        return true
    
def filtraMultiplos(ls,n):
    for e in ls:
    
    return filtra(ls, multiplo(ls,n))