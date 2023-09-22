def fatorial(n):
    '''Essa função dado um número calcula o fatorial desse número;
    Recebe um número
    Retorna o resultado do fatorial desse número
    int->int'''
    r = 1
    for i in range(1,n+1):
        r *= i
    return r
#Essa função dado um número calcula o fatorial desse número