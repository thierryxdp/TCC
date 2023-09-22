def qtd_divisores(num):
    '''função que conta quantos divisores um numero tem; int->float'''
    cont = 2
    for  i in range(1,num+1):
        if num % i == 0:
            cont = cont + 1
        return cont