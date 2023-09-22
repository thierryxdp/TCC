def posLetra(string,letra,numero):
    ocorrencia = 0
    letra = 0
    while letra < len(string):
        if string[letra] in 'abcdefghijklmnopqrstuvxwyzç':
            ocorrencia = ocorrencia + 1
        letra = letra + 1
    return ocorrencia
        else:
            return -1