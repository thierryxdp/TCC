def filtraMultiplos(lista,n):
    '''' '''
    lista_nova= []
    indice=0  
    while lista[indice]%n != 0:
        lista.remove(lista[indice])
        indice = indice + 1
    return lista