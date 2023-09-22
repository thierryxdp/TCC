def acima_da_media(lista):
    media = sum(lista)//len(lista)
    maiores2 = maiores(lista,n)
    if media in maiores2: #Caso a média seja igual a um valor dentro da lista, vamos retirar o valor da média
        list.remove(maiores2,media)
        return maiores2
    
    else:
	return maiores2

def maiores(lista, n):
    '''A função retornará uma lista com apenas os números maiores que (n).
    
    dados de entrada -> lista, int
    dados de saída -> lista'''
    n = 5
    
    list.append(lista,n) #inserindo o numero (n) no final da lista
    list.sort(lista) #colocando os números em ordem crescente
    posicao = list.index(lista,n) #descobrindo a posição do numero n na lista ordenada
    
    return lista[posicao+1:] #fatiamento da lista com os números maiores que n