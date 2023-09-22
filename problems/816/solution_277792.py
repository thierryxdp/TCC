def maiores(lista, n):
    """Função que irá receber uma lista de números inteiros e um número inteiro n e retornará outra lista contendo os números da lista original maiores que n.
    	
        Parameters:
        lista: lista ordenada com números inteiros
        n: número inteiro
    
		Returns:
        nova lista com os núemros da lista original maiores que n
        
    list, int -> list
    """
    
    nova_lista = lista [:]
    list.append(nova_lista, n)
    list.sort(nova_lista)
    index = list.index(nova_lista, n)
    return nova_lista[index+1:]