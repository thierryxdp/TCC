def qtd_divisores(x):
    '''função que conta quantos divisores um número x fornecido pelo usuário tem.'''
    cont = 0
    for i in range(1, x+1):
        if x % i == 0:
            cont = cont + 1
    return cont