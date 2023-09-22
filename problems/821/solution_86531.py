def fatorial(numero):
    '''Calcula e retorna o fatorial de um numero qualquer
       parameters:
       numero: numero que sera definido seu fatorial
       int->int'''
    proximo=0
    while numero > 1:
        fatorial=proximo*numero
    proximo=proximo+1
    return fatorial