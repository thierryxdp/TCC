def filtraMultiplos(lista,n):
    '''' '''
    lista_nova= []
    indice=0  
    while lista[indice]%n != 0:
        remove=lista.pop(indice)
        indice = indice + 1
    return lista