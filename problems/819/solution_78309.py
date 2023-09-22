lista2=[]
def filtraMultiplos(lista,n):
    i=0
    k=len(lista)
    while i<k:
        a=lista[i]%n
        if a==0:
            lista2=lista2+list(lista[i])
        i=i+1
    return lista2