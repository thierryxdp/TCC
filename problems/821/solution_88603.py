def fatorial(numero):
    '''---'''
    fatoracao = 1
    indice = 1
    while indice <= numero:
        fatoracao *= indice
        indice += 1
    return fatoracao