def filtraMultiplos(lista,n):
    i=0
    lista=[]
    while lista[i]%n==0:
        lista=lista+lista[i]
        i+=1
    return lista