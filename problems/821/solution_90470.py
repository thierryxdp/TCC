def fatorial(x):
    '''uma funcao que dado um numero, calcula o fatorial do mesmo
    int -> int'''
    contador = 1
    fator = 1
    while contador <= x:
        fator = fator*contador
        contador += 1
    return fator