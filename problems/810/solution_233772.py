def inverte(frase):
    frase=frase.replace('?', ' ')
    frase=frase.replace('!', ' ')
    frase=frase.replace('-', ' ')
    frase=frase.replace('.', ' ')
    frase=frase.replace(',', ' ')
    frase=frase.lower()
    return str.join(' ',frase.split()[::-1])