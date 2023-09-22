def maiores(lista, n):
    """função que dada uma lista com números inteiros, retorna outra lista contendo todos os números
	maiores que n.
	list, int -> list"""
    
    maiores_numeros = list()
    for c in lista:
        if c > n:
            maiores_numeros.append(c)
	
    list.sort(maiores_numeros)
    
    return maiores_numeros