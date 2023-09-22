def inverte(frase):
    frase=frase.replace('?', ' ')
    frase=frase.replace('!', ' ')
    frase=frase.replace('-', ' ')
    frase=frase.replace('.', ' ')
    frase=frase.replace(',', ' ')
    return frase.join(frase.split())[::-1]