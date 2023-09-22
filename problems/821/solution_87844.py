def fatorial(numero:int)->int:
    """ A função recebe um número, e deve retornar o fatorial desse número"""
    numero = list(range(numero + 1))
    indice = 0
    fatorial = 0
    while indice < len(numero):
        fatorial *= numero[indice]
    
    i = i + 1
    
    return fatorial