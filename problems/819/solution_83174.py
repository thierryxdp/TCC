def filtraMultiplos(lista,n):
    '''' '''
    lista_nova= []
    indice=0  
    while ista[indice]%n != 0:
        if lista[indice]%n != 0:
           	lista.pop(indice)
            indice +=1
    return lista