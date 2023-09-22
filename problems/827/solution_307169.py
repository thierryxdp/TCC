def qtd_divisores (n):
    '''
    A função retorna quantos devisores 
    o número de entrada tem
    '''
    if n < 0:
        return 0
    else:
        a = 100
        i = 1
        l = []
        while a > 1:
            l += [a]
            a -= 1
        for x in l:
            if n % x == 0:
                i += 1
        return i