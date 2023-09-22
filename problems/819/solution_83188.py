def filtraMultiplos(lista,n):
    ''''Função que pega os valores da lista de entrada e identifica e retorna os valores divisíveis pelo valor n de entrada.
    	list, list→list'''
    lista_nova= []
    indice=0  
    while indice < len(lista):           
        if lista[indice]%n ==0:
            lista_nova.append(lista[indice])
        if indice == len(lista):
            break
        indice+=1
    return lista_nova