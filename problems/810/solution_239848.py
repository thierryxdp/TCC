def inverte(frase):
    frase = frase.replace('!', ' ')
    frase = frase.replace('?', ' ')
    frase = frase.replace(',', ' ')
    frase = frase.replace('.', ' ')
    frase = frase.replace(';', ' ')
    frase = frase.replace(':', ' ')
    frase = frase.replace('-', ' ')
    return ' '.join(frase.split()[::-1])