def maiores(lista,n):
    '''retorna todos os numeros inteiros maiores que n'''
    if lista[0]>n:
        return list.sort(lista)
    else:
        return []