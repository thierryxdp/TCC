def filtraMultiplos(lista,n):
    proximo=0            
    lista_nova=[]
    while proximo<len(lista):
        if lista[proximo]%n==0:
            lista_nova=lista_nova+list(lista[proximo])
        proximo=proximo+1
    return lista_nova