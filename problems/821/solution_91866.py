def fatorial(numero):
    resultado = numero
    numero_auxiliar = numero
    
    while numero_auxiliar > 1:
        numero_auxiliar -= 1
        resultado *= numero_auxiliar
    
    return resultado