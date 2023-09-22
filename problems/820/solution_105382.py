def posLetra(frase,letra,ocorrencia):
    ''''''
    pos = frase.find(letra)
    while pos >= 0 and ocorrencia > 1:
        pos = frase.find(letra, pos + 1)
        ocorrencia -= 1
    return pos