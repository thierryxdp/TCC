def fatorial(numero):
    multiplicador = 1
    resultado = 1
    while multiplicador <= numero:
        resultado = numero* multiplicador
        multiplicador = multiplicador + 1
    return resultado