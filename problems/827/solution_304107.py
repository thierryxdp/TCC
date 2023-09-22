def qtd_divisores(num):
    '''função que conta quantos divisores um numero tem; int->float'''
    qtd = 1
    for  i in range(1,num+1):
        if num % i == 0:
            qtd =+ 1
        return qtd