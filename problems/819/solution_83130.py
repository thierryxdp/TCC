def filtraMultiplos(lista,n):
    '''' '''
    lista_nova= []
    indice=0  
    while lista[indice]%n == 0:
        lista_nova.append(lista[indice])
        indice = indice + 1
        break
    return lista_nova