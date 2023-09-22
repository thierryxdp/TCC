def fatorial(n):
    '''função que dado numero n, calcula o fatorial desse
    numero.  ent-> int  saida-> int'''
    
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num