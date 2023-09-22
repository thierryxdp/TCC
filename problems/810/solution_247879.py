def inverte(frase):
    frase = str.lower(frase)
    ponto = frase.replace(".","").replace(",","").replace("!","").replace("?","")
    dividida = ponto.split(" ")
    inverso = dividida[::-1]
    return inverso