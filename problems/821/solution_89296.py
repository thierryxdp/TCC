def fatorial(num):
    '''retorna o valor fatorial do numero. int->int'''
    contador= num
    fator=num
    while contador-1 != 0:
        fator = fator*(contador-1)
        contador= contador-1
    return fator