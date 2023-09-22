def inverte(frase):
    frase = str.lower(frase)
    frase = str.replace(frase, ",", "")
    frase = frase[:-1]
    
    return frase[-1:0]