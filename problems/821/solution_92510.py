def fatorial(numero):
    '''essa função calcula o fatorial de um numero qualquer
    int -> int'''
    multiplicacao = 1
    for x in range(1, (numero+1)):
        multiplicacao = multiplicacao * x  
    return multiplicacao