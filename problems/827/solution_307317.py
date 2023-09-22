def qtd_divisores(num):
    '''função que conta quantos divisores um numero tem; int->float'''
    cont = 1
    for  n in range(1,num+1):
        if num % n == 0:
            cont = cont + 1
        return cont