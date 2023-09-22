def maiores(lista,n):
    '''função que dada uma lista de números e dado um número
    inteiro n como entrada, retornará uma outra lista
    com os números da lista original maiores que n, em ordem
    crescente.
    str -> str'''
    maiores_num = list()
    for c in lista:
        if c >= n:
            maiores_num.append(c)
    return maiores_num