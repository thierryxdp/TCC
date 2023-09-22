def conta_frases(texto):
    if str.find(texto, ',')==True:
        texto= str.replace(texto, ',', '')
        return texto