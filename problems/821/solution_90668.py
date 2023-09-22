def fatorial(numero):
    
    resultado = 1
    while numero > 0:
        resultado = resultado * (numero -1)
        numero -= 1
    return resultado