def fatorial(numero):
    '''Calcula e retorna o fatorial de um numero qualquer
       parameters:
       numero: numero que sera definido seu fatorial
       int->int'''
    proximo=0
    while numero>1:
        fator=numero*proximo
        proximo=proximo+1
    return fator