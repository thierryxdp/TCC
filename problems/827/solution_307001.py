def qtd_divisores(numero):
    '''função que conta quantos divisores um numero tem; int->float'''
    cont = 1
    for  i in range(1,numero//2+1):
        if numero % i == 0:
            cont = cont + 1
    return cont