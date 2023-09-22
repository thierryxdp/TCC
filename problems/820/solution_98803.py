def posLetra(entrada, letra, ocorrencias):
    contador = 0
    indice = 0
    while indice < len(entrada):
        if entrada[indice] == letra:
            contador += 1
        if contador == ocorrencias:
            return indice
        indice += 1
    return -1