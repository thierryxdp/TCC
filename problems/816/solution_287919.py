def maiores(lista,n):
    '''Retorna uma lista com todos os números da lista original maiores que n, em ordem crescente.
    list,int-->list'''
    if max(lista)<n:
        list.clear(lista)
    elif min(lista)>n:
        list.sort(lista)
    return lista