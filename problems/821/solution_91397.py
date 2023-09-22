def fatorial(numero):
    '''calcula o fatorial desse numero
    int-->int'''
    n=0
    resultado=1
    while numero-n > 0:
        resultado=resultado*(numero-n)
        n=n+1
    return resultado