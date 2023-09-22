def qtd_divisores (n):
    '''
    A função retorna quantos devisores 
    o número de entrada tem
    '''
    l = [1, 2, 3, 5, 7]
    i = 1
    for x in l:
        if n % x == 0:
            i += 1
    return i