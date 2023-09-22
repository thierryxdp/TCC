def inverte(frase):
    frase = frase.replace('.','')
    frase = frase.replace('!','')
    frase = frase.replace('?','')
    frase = frase.replace(',','')
    frase = frase.replace('-','')
    frase = frase.replace(':','')
    frase = frase.replace(';','')
    frase = frase.lower()
    frase = list(frase.reverse())
    return frase