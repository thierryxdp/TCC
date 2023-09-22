def fatorial (numero):
    """ retorna o fatorial do numero"""
    n = numero 
    contador = 1
    while n > 0:
        contador *= n
        n -= 1
    return contador