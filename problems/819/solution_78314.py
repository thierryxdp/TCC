lista2=[]
def filtraMultiplos(lista,n):
    i=0
    k=len(lista)
    while i<k:
        if lista[i]%n==0:
            lista2=lista2+lista[i]
        i=i+1
    return lista2