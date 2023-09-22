def fatorial(numero):
    '''Recebe um numero (numero) e retorna o
    seu fatorial
    
    int -> int
    '''
    contador = 1
    fatorial = numero
    
    while contador < numero:
        fatorial = fatorial*contador
        contador += 1
    return fatorial