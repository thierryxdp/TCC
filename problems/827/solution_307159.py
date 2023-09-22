def qtd_divisores (n):
    '''
    A função retorna quantos devisores 
    o número de entrada tem
    '''
    if n < 0:
        return 0
    else:
        i = 2
        l = [2, 3, 5, 7]
        for x in l:
            if n % x == 0:
                i += 1
        return i