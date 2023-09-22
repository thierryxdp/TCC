def maiores(lista,n):
    '''dado uma lista de inteiros, e um numero. retorna os valores
da lista, ordenados de modo crescente, maiores que esse numero.
    list,int->list'''
    a=([i for i in lista if i > n])
    return sorted(a)