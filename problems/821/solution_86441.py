def fatorial(numero):
    '''Calcula e retorna o valor fatorial de um numero qualquer
       parameters:
       numero: numero inteiro e positivo qualquer
       int->int'''
    proximo=0
    multiplicaçao=0
    while numero > 0:
        if proximo > 0 and proximo < numero:
            multiplicaçao=numero * proximo
            proximo=proximo + 1
    return multiplicaçao