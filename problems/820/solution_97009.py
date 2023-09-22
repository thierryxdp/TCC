def posLetra(string,letra,numero):
    ocorrencia = 0
    letra = 0
    while letra < len(string):
        if string[letra] in string:
            ocorrencia = ocorrencia + 1
        letra = letra + 1
    return ocorrencia