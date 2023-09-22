def maiores(lista,n):
    """
    	Retorna uma lista com os elementos da lista dada maiores que n
    	list,int -> list
    """
	if not(n in lista):
        list.append(lista,n)
    list.sort(lista)
	return lista[list.index(lista,n)+1:]

def acima_da_media(lista_notas):
    """
    	Retorna uma lista com as notas acima da média
    	list -> list
    """
    media = sum(lista_notas)/len(lista_notas)
    return maiores(lista_notas,media)