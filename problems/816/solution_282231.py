def maiores (lista, n):
    '''
    	essa função recebe uma lista de numeros e retorna outra lista contendo todos os 
        numeros da lista original maiores que n, em ordem crescente 
        list,int->list
    '''
    lista.append(n)
    lista.sort()
    x = lista.index(n)+1
    
    return lista[x:]