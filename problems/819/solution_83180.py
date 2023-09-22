def filtraMultiplos(lista,n):
    '''' '''
    lista_nova= []
    indice=0  
    while lista[indice]%n != 0:
        if indice <= len(lista):
			lista.pop(indice)
			indice +=1
    return lista