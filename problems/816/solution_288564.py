def maiores(lista,n):
    '''Retorna uma lista com todos os números da lista original maiores que n, em ordem crescente.
    list,int-->list'''
    list.append(lista,n)
    list.sort(lista,reverse=True)
    a=list.index(lista,n)
    b=lista[0:a]
    
    return b