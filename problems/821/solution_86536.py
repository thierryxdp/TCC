def fatorial(numero):
    '''Calcula e retorna o fatorial de um numero qualquer
       parameters:
       numero: numero que sera definido seu fatorial
       int->int'''
    proximo=0
    resultado=0
    while numero > 1 and numero>proximo:
        fatorial=proximo*numero
        proximo=proximo+1
        resultado=resultado*fatorial
    return resultado