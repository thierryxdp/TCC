def fatorial(x):
    '''uma função que dado um número, calcula o fatorial deste mesmo número.
    float -> float'''
    contador = 0
    fator = 0
    while contador < x:
        fator = fator*contador
        contador =+ 1
    return fator