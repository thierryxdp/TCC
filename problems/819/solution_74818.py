def filtraMultiplos(lista,n):
    lista=[]
    x=0
    while x<=len(lista)-1:
        if lista[x]%n==0:
        	lista.append(lista[x])
        x=x+1
    return lista