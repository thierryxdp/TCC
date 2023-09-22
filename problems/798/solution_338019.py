def freq_palavras(frases):
    i=0
    valor = []
    while i < len(str.split(frases)):
        valor = valor + str.split(frases)[i]
    return valor