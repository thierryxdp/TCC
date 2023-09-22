def posLetra(string, letra, ocorrencia):
    i = 0
    posicao = 0
    while i < len(string):
        if letra in string:
            posicao = string[letra]
            i = i+1
        else:
            if letra not in string:
                return -1
    return posicao