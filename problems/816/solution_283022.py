def maiores(lista,n):
    '''A função recebe uma lista e um inteiro n, e retorna uma nova lista com todos 
    os elementos maiores que n na lista original; ordem crescente.
    	list , int -- > list'''
    
    lista.sort()
	if lista[0] < n:
        lista.remove(lista[0])
        return maiores(list a,n)
    return lista