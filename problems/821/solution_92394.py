def fatorial(numero):
    '''essa função faz a conta do fatorial de um numero
    int -> int'''
    multiplicacao = 1
    for i in range(1, (numero+1)):
        multiplicacao = multiplicacao * i  
    return multiplicacao