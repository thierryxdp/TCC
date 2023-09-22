def filtraMultiplos(lista,n):
    proximo=0            
    lista_nova=[]
    while proximo<len(lista):
        if lista[proximo]%n==0:
            lista_nova=lista_nova+[lista[poximo],]
        proximo=proximo+1
    return lista_nova