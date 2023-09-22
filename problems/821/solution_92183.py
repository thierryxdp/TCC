def fatorial(numero):
    ''' funcao que dado um numero retorna seu fatorial 
    int -> int'''
    contando = 1
    fatorial = 1
    while contando <= numero:
        fatorial*= contando 
        contando = contando +1 
    return fatorial