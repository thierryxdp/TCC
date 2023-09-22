def filtraMultiplos(lista,n):
    a=0
    proximo=lista[a]              
    lista_nova=0
    while proximo%n==0:
        a=a+1
        proximo=lista[a]
        lista_nova=lista_nova+list(proximo)
        return lista_nova