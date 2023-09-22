def maiores(lista, n):
    '''A função retornará uma lista com apenas os números maiores que (n).
    
    lista, int-> lista'''
    
    list.append(lista,n) #inserindo o numero (n) no final da lista
    list.sort(lista) #colocando os números em ordem crescente
    posicao = list.index(lista,n) #descobrindo a posição do numero n na lista ordenada
    
    return lista[posicao+1:] #fatiamento da lista com os números maiores que n