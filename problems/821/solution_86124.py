def fatorial(numero):
    Numero = list(range(10))
    contador = 1
    resultado = 1
    while contador<=len(range(10)):
          resultado = resultado * contador
          contador = contador + 1
    return resultado