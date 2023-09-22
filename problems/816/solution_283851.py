def maiores(lista, n):
    '''
    	Função que retorna uma lista que contem todos os 
        núemeros da lista dada maiores que n, em ordem 
        crescente.
    	list,int -> list
    '''
    lista.append(n)
    lista.sort()
    pos = lista.index(n)
    return pos