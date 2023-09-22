def posLetra(string, letra, numero):
    contador = 0
    acumulador = (0)
    while contador < numero:
        posicao = str.find(string, letra)
        acumulador = acumulador + posicao,
        contador = contador + 1
    return posicao