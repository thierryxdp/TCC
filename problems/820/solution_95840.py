'''Retorna a posicao da ultima ocorrencia de uma letra em um texto dado'''
#str, str, int -> int
def posLetra(texto, letra, ocorrencia):
    contador = 0
    acumulador = 0
    posicao = 0
    while contador < len(texto) and acumulador < ocorrencia:
        if texto[contador] == letra:
            posicao = contador
            acumulador = acumulador + 1
        contador = contador + 1
    if ocorrencia > acumulador:
        return - 1
    else:
        return posicao