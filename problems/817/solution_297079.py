def acima_da_media(lista):
    """Função que recebe uma lista, calcula a média
    dos elementos na lista e retornar uma
    lista com todos os elementos da lista que são
    acima da média do somatório de todos os 
    elementos da lista"""
   	maiores(lista, numero):
 	   """Função que recebe uma lista, um número que é
    	inserido na lista e retorna uma lista com todos
    	os números maiores que o número inserido
    	list, int -> list"""
    	list.append(lista,numero)
    	list.sort(lista)
    	return lista[list.index(lista,numero)+1:]

    media = sum(lista)/len(lista)
    
    if not(media in lista):
        return maiores(lista,media)
    else:
    	
        lista2 = maiores(lista,media)
        return lista2[1:]