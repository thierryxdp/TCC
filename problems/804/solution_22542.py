#Start your python function here
def filtra_pares(a, b, c, d):
    '''Dada uma tupla com quatro elementos inteiros a, b, c e d, retorna uma nova tupla contendo apenas os elementos pares, na mesma ordem em que se encontravam na tupla original;
	assinatura: int, int, int, int --> tuple(...)
    Casos de teste:
    filtra_pares(1, 2, 3, 4) == (2, 4)
    filtra_pares(4, 3, 2, 1) == (4 ,2)
    filtra_pares(0, -5000, 199, 200) == (0, -5000, 200)'''
    if (a % 2) == 0 and (b % 2) == 0 and (c % 2) == 0 and (d % 2) == 0:
        return (a, b, c, d)
    elif (a % 2) == 0 and (b % 2) == 0 and (c % 2) == 0:
        return (a, b, c)
    elif (a % 2) == 0 and (b % 2) == 0 and (d % 2) == 0:
        return (a, b, d)
    elif (a % 2) == 0 and (c % 2) == 0 and (d % 2) == 0:
        return (a, c, d)
    elif (a % 2) == 0 and (b % 2) == 0:
        return (a, b)
    elif (a % 2) == 0 and (c % 2) == 0:
        return (a, c)
    elif (a % 2) == 0 and (d % 2) == 0:
        return (a, d)
    elif (a % 2) == 0:
        return (a)
    elif (b % 2) == 0 and (c % 2) == 0 and (d % 2) == 0:
        return (b, c, d)
    elif (b % 2) == 0 and (c % 2) == 0:
        return (b, c)
    elif (b % 2) == 0 and (d % 2) == 0:
        return (b, d)
    elif (b % 2) == 0:
        return (b)
    elif (c % 2) == 0 and (d % 2) == 0:
        return (c, d)
    elif (c % 2) == 0:
        return (c)
    elif (d % 2) == 0:
        return (d)
    else:
        return ()