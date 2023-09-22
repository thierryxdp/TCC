def posLetra(string,letra,numero):
    ocorrencia = 0
    letra = 0
    while letra < len(string):
        if string[letra] in string[numero]:
            ocorrencia = ocorrencia + 1
        letra = letra + 1
            print (ocorrencia)
    else:
        return -1