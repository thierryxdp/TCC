def qtd_divisores (n):
    '''
    A função retorna quantos devisores 
    o número de entrada tem
    '''
    l = [2, 3, 4, 5, 6, 7, 8, 9]
    i = 2
    for x in l:
        if n % x == 0:
            i += 1
    return i