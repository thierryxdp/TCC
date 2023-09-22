def fatorial(x):
    '''uma função que dado um número, calcula o fatorial deste mesmo número.
    float -> float'''
    contador = 1
    fator = 1
    while contador <= x:
        fator = fator*contador
        contador = contador + 1
    return fator