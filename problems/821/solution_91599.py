def fatorial (x):
    '''retorna o fatorial de um numero x de entrada
    int -> int'''
    fatorial=1
    fator=1
    while fator <= x:
        fatorial *= fator
        fator +=1
    return (fatorial)