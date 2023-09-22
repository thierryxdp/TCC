def inverte(frase):
    frase2 = ''
    frase = frase.replace('.', ' ')
    frase = frase.replace('-', ' ')
    frase = frase.replace(',', ' ')
    frase = frase.replace(':', ' ')
    frase = frase.replace('!', ' ')
    frase = frase.replace('?', ' ')
    frase = frase.replace(';', ' ')
    for palavra in frase.split()[::-1]:
        frase2 = frase2 + palavra + ' '
    return frase2.strip().lower()