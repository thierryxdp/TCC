def posLetra(string, letra, numero):
    contador = 0
    acumulador = ()
    while contador < numero:
        posicao = str.find(string, letra, letra[acumulador[::-1]], range(string))
        acumulador = acumulador + (posicao,)
        contador = contador + 1
    return posicao