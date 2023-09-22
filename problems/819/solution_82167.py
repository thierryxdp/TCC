def filtraMultiplos(lista,n):
    
    lista=[]
    b=len(lista)
    for(i=0,i<b,i++):
        while lista[i]%n:
            lista=lista+lista[i]
    return lista