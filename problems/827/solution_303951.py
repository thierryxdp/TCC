def qtd_divisores(num):
    '''função que conta quantos divisores um numero tem; int->float'''
    num >= 0
    cont = 1
    for  i in range(1,num//2+1):
        if num % i == 0:
            cont = cont + 1
        return cont