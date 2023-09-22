acima_da_media(lista):
    list.append(lista,5) #inserindo o numero (n) no final da lista
    list.sort(lista) #colocando os números em ordem crescente
    posicao = list.index(lista,5) #descobrindo a posição do numero n na lista ordenada
    
    maiores = lista[posicao+1:] #fatiamento da lista com os números maiores que n
    media = sum(lista)//len(lista)
    if media in maiores: #Caso a média seja igual a um valor dentro da lista, vamos retirar o valor da média
        list.remove(maiores,media)
        return maiores
    
    else:
	return maiores