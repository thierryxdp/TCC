def fatorial(n):
    '''Dado um número, a função retorna o fatorial desse número
    int->int'''
    
    num = 1
    while n >= 1:
        num=num*n
        n= n-1
    return num