def qtd_divisores(x):
    '''retorna a quantidade de divisores que um numero de entrada x tem
    int -> int'''
    if x <= 0:
        return 0
    qtd = 0
    for i in range(1,x):
        if x%i == 0:
            qtd += qtd + 1
            return qtd