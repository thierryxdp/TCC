def filtraMultiplos(lista,n):
    x=1
    while x<=len(lista)-1:
        if not lista[x]%n==0:
        	lista.remove(lista[x])
        x=x+1
    return lista