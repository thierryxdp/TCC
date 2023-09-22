lista2=[]
def filtraMultiplos(lista,n):
    i=0
    k=len(lista)
    d=len(lista)//2
    while i<k:
        a=lista[i]%n
        if a==0:
            list.append(lista2,lista[i])
        i=i+1
    return lista2[0:d]