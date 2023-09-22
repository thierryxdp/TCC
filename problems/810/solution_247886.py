def inverte(frase):
    frase = str.lower(frase)
    ponto = frase.replace(".","").replace(",","").replace("!","").replace("?","").replace("-","")
    dividida = str.split(ponto," ")
    inverso = dividida[::-1]
    return inverso.replace(","," ")