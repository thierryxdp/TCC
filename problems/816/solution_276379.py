def maiores(lista,n):
    '''retorna todos os numeros inteiros maiores que n'''
    list.sort(lista)
    if lista[0]>n:
        return lista
    else:
        return []