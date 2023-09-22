def fatorial(numero:int)->int:
    """ A função recebe um número, e deve retornar o fatorial desse número"""
    numero = list(range(numero + 1))
    numero = numero[1:]
    indice = 0
    fatorial = 1
    while indice < len(numero):
        fatorial = fatorial * numero[indice]
        
        indice = indice + 1
    
    return fatorial