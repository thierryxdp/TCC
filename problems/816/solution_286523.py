def maiores(lista,n):
    '''
       Dada uma lista e um número n retorna uma nova lista
       apenas com os números maiores que n em ordem crescente
       list, int -> list
    '''
    maiores_num = list()
    for c in lista:
        if c >= n:
            maiores_num.append(c)
            maiores_num.sort(c)
    return mariores_num