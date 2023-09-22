def inverte(frase):
    frase = frase.lower()
    frase = frase.replace(".","")
    frase = frase.replace("!","")
    frase = frase.replace(",","")
    frase = frase.replace("?","")
    
    nfrase = frase.split()
    invertida = nfrase[::-1]
    invertida = ' '.join(invertida)
    return invertida