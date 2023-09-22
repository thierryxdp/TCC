def inverte(frase):
    frase = frase.replace('/', ' ')
    frase = frase.replace(',', ' ')
    frase = frase.replace(':', ' ')
    frase = frase.replace(';', ' ')
    frase = frase.replace('.', ' ')
    frase = frase.replace('-', ' ')
    frase = frase.replace('?', ' ')
    frase = frase.replace('!', ' ')
    frase = frase.split()
    frase = frase[::-1]
    fraseinvertida = ''.join(frase)
    return fraseinvertida