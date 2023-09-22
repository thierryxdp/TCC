def inverte(frase):
    frase = frase.replace('.','')
    frase = frase.replace('!','')
    frase = frase.replace('?','')
    frase = frase.replace(',','')
    frase = frase.replace('-','')
    frase = frase.replace(':','')
    frase = frase.replace(';','')
    frase = frase.lower()
    frase = frase.split()
    
    return frase.reverse()