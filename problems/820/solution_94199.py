def posLetra(string,letra,ocorrencia):
    x=0
    contador=0
    while x<len(string) and contador<ocorrencia:
        if string[x]==letra:
            contador = contador + 1
            x = x + 1
    if contador<ocorrencia:
        return "foram encontradas" + str(contador) + "ocorrencias de" + str(letra)
    else:
        return i-1