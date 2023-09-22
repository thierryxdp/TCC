def fatorial(x):
    '''retorna o fatorial de um numero de entrada x'''
    fatorial=1
    numero = 1
    while x>1:
        fatorial*=numero
        numero +=1
    return fatorial