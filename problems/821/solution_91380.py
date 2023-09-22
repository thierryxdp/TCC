def fatorial(numero):
    resultado = 1
    contador = 1
    while contador <= numero:
        resultado *= contador
        contador  = contador + 1
    return resultado