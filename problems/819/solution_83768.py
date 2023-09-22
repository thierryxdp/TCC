def filtra_multiplos(lista,n):
    proximo=lista[0]
    lista_nova=0
    while proximo%n==0:
        proximo=lista[0+1]
        lista_nova=lista_nova+proximo
    return lista_nova