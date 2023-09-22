def maiores(lista,n):
    '''Funcao que calcula e retorna uma lista de numeros inteiros maiores que n.
    int->int'''
       maiores = list()
    for c in lista:
        if c >= n:
            maiores.append(c)
    return maiores