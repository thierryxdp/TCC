def fatorial(numero):
    '''Calcula e retorna o fatorial de um numero qualquer
       parameters:
       numero: numero que sera definido seu fatorial
       int->int'''
    proximo=numero
    while proximo>1:
        fator=numero*proximo
        proximo=numero-1
    return fator