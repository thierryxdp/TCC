def filtra_pares(x):
    '''recebe uma tupla de quatro elementos inteiros e retorna uma nova tupla contendo apenas os elementos pares da tupla original na mesma ordem que eles se encontravam
    casos de teste:
    filtra_pares([828,9018,647,917]) == (828,9018)
    filtra_pares([1,2,3,4]) == (2,4)
    filtra_pares([1,3,5,7]) == ()
    '''
    tupla  = ()
    elem_1 = int(x[0])
    elem_2 = int(x[1])
    elem_3 = int(x[2])
    elem_4 = int(x[3])

    if elem_1 % 2 == 0:
        tupla = tupla + (elem_1,)
    if elem_2 % 2 == 0:
        tupla = tupla + (elem_2,)
    if elem_3 % 2 == 0:
        tupla = tupla + (elem_3,)
    if elem_4 % 2 == 0:
        tupla = tupla + (elem_4,)
    return tupla