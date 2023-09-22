def filtraMultiplos(lista,n):
    '''' '''
    lista_nova= []
    indice=0  
    while lista[indice]%n == 0:
        indice = indice + 1
        lista_nova.append(lista[indice])
    return lista_nova