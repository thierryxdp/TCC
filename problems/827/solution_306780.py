def qtd_divisores (n):
    '''
    	essa função recebe um número e retorna a quantidade de divisores que a mesma tem
        int->int
    '''
    if n = 1:
        return 1
    x = 1
    for el in range(1, n):
        if n % el == 0:
            x = x + el[n]
    return x