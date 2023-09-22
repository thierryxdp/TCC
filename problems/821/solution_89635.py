def fatorial(numero):
    '''funcao que, dado um numero, retorna o seu fatorial;
    int->int'''
    fatorial = 1
    while (numero > 0):
        fatorial = fatorial * numero
        numero = numero - 1
    return fatorial