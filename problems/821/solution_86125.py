def fatorial(numero):
    Numero = list(range(numero))
    contador = 1
    resultado = 1
    while contador<=len(range(numero)):
          resultado = resultado * contador
          contador = contador + 1
    return resultado