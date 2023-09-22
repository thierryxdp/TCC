def maiores(lista,n):
    '''retorna todos os numeros inteiros maiores que n'''
    s=list.sort(lista)
    if lista[0]>n:
        return s
    else:
        return []