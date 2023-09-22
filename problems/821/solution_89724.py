def fatorial(numero):
    '''
       função que, dado um numero, calcula o fatorial desse 
       numero
       int -> int
    '''
    i = 1
    resultado=1
    while i < numero:
        resultado = resultado*i
        i=i+1
    return resultado*numero