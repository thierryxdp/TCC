def maiores(lista,n):
    '''A função recebe uma lista e um inteiro n, e retorna uma nova lista com todos 
    os elementos maiores que n na lista original; ordem crescente.
    	list , int -- > list'''
    
    lista_ordenada = lista.sort()
    
    
    nova_lista = []
    for i in lista_ordenada:
        if i > n:
            nova_lista.append(i)
    return nova_lista