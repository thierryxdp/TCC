def maiores(listanumeros, n):
    '''funcao que retorna uma lista que contenha todos 
    os numeros da lista original maiores que n;list->list'''
    list.append(listanumeros, n)
    list.sort(listanumeros)
    h=list.index(listanumeros, n)
    return listanumeros[h+1:]