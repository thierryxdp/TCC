def posLetra(string, letra, numero):
    contador = 0
    acumulador = (0,)
    fim = (len(string)-1)
    inicio = len(acumulador)
    while contador < numero:
        posicao = str.find(string, letra, inicio, fim)
        acumulador = acumulador + (posicao,)
        contador = contador + 1
    return posicao