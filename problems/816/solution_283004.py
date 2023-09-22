def maiores(lista,n):
    '''A função recebe uma lista e um inteiro n, e retorna uma nova lista com todos 
    os elementos maiores que n na lista original; ordem crescente.
    	list , int -- > list'''
    
    nova_lista = []
    for i in lista:
        if i > n:
            nova_lista.extend(i)
    return nova_lista