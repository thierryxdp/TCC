def multiplo(m,n):
    resp = True if m%n ==0 else False
    return resp

def filtraMultiplos(lista,n):
	resp = filter(multiplo(n=n),lista)
    return resp