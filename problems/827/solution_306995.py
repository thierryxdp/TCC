def qtd_divisores(num):
    '''função que conta quantos divisores um numero tem; int->float'''
    d = 1
    for  i in range(1,num//2+1):
        if num % i == 0:
            d = d + 1
    return d