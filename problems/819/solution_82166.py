def filtraMultiplos(lista,n):
    
    lista=[]
    i=len(lista)-1
    while lista[i]%n==0:
        lista=lista+lista[i]
        i-=1
    return lista