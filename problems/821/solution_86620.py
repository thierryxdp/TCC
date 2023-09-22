def fatorial(numero):
    '''Calcula e retorna o fatorial de um numero qualquer
       parameters:
       numero: numero que sera definido seu fatorial
       int->int'''
    fator=1
    proximo=1
    while numero>0 and proximo<=numero:
        fator=fator*proximo
        proximo=proximo+1
    return fator