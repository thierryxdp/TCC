lista2=[]
def filtraMultiplos(lista,n):
    i=0
    k=len(lista)
    while i<k:
        a=lista[i]%n
        u=list(lista[i])
        if a==0:
            lista2=lista2+u
        i=i+1
    return lista2