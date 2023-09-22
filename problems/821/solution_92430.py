def fatorial(numero):
    contador = 1
    resultado = numero * contador
    while contador < numero:
        resultado *= contador
        contador += 1
    else:
        return resultado