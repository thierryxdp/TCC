def maiores(lista,n):
    '''A função recebe uma lista e um inteiro n, e retorna uma nova lista com todos 
    os elementos maiores que n na lista original; ordem crescente.
    	list , int -- > list'''
    
    lista.sort()
	nova_lista = lista [n+1:]
    return nova_lista