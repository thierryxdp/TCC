def maiores(lista,n):
    '''Retorna uma lista que contem todos os numeros inteiros maiores que n, dados uma lista de numeros inteiros e um numero inteiro
    list,int->list'''
    a=([i for i in lista if i > n])
    return sorted(a)