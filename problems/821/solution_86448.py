def fatorial(numero):
    '''Calcula e retorna o valor fatorial de um numero qualquer
       parameters:
       numero: numero inteiro e positivo qualquer
       int->int'''
    proximo=0
    multiplicacao=0
    while numero > 0:
        if proximo >0:
            multiplicacao=numero * proximo
            proximo=proximo + 1
    return multiplicacao