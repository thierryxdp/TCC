def posLetra(string, letra, ocorrencia):
    posLetra = string.find(letra)
    while posLetra >= 0 and ocorrencia > 1:
        posLetra = string.find(letra, posLetra + 1)
        ocorrencia -= 1
    return posLetra