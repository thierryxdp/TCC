def maiores(lista,n):
    '''retorna outra lista que contenha todos os números da lista original maiores que n. list,int->list'''
    list.append(lista,n)
    list.sort(lista)
    del lista[:list.index(lista,n)+1]
    return lista