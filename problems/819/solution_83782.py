def filtraMultiplos(lista,n):
    proximo=0            
    lista_nova=0
    while lista[proximo]!=0:
         if lista[proximo]%n==0:
        proximo=proximo+1
        lista_nova=lista_nova+list(lista[poximo])
    return lista_nova