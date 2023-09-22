def filtraMultiplos(lista,n):
    proximo=lista[a]
    a=0              
    lista_nova=0
    while proximo%n==0:
        a=a+1
        proximo=lista[a]
        lista_nova=lista_nova+proximo
        return lista_nova