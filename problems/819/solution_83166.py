def filtraMultiplos(lista,n):
    '''' '''
    lista_nova= []
    indice=0  
    while indice<= len(lista):
        if lista[indice]%n != 0:
            lista.pop(indice)
            indice +=1
    return lista