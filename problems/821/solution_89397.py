def fatorial(numero):
    """ faz o fatorial do numero inserido
            int --> int"""
    i = 2
    resultado = 1
    while i <= numero:
        resultado = resultado * i
        i=i+1
    return resultado