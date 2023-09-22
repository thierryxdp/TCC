def filtra_pares(x):
    '''recebe uma tupla de quatro elementos inteiros e retorna uma nova tupla contendo apenas os elementos pares da tupla original na mesma ordem que eles se encontravam
    '''
    tupla()
    elem_1 = int(x[0])
    elem_2 = int(x[1])
    elem_3 = int(x[2])
    elem_4 = int(x[3])

    if elem_1 % 2 == 0:
        tupla = tupla + (elem_1,)
    if elem_2 % 2 == 0:
        tupla = tupla + (elem_2,)
    if elem_3 % 2 == 0:
        tupla = tupla + (elm_3,)
    if elem_4 % 2 == 0:
        tupla = tupla + (elem_4,)
    return tupla