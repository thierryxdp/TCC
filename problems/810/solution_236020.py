def inverte(frase):
    frase = frase.replace('.', '').replace('?', '').replace('!', '').replace(';', '').replace(':', '').replace(',',' ').replace('-','')
    frase = frase.lower()
    frase = frase.split()
    frase = frase[-1::-1]
    frase = str.join(' ',frase)
    return frase