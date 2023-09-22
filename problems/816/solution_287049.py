def maiores(lista,n):
    '''essa funçao contem uma lista original e retorna uma outra lista com todos os numeros dessa lista original maiores que n
    list, int -> lista'''
    
    list.sort(lista)
    if n <lista[0]:
        return lista[ : ]
    else:
        list.append(lista,n)
        list.sort(lista)
        posicao=list.index(lista,n)+1
        del lista[0:posicao]
        
        return lista