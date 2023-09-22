def multiplo(m):
    resp = True if m%n ==0 else False
    return resp

def filtraMultiplos(lista,n):
	resp = filter(multiplo,lista)
    return resp