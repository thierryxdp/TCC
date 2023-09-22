def inverte(frase):
    '''   '''
    frase = frase.replace('!', ' ')
    frase = frase.replace('?', ' ')
    frase = frase.replace('-', ' ')
    frase = frase.replace('.', ' ')
    frase = frase.replace(':', ' ')
    frase = frase.replace(';', ' ')
    frase = frase.replace(',', ' ')
    frase = str.lower(frase)
    frase = frase.split(' ')
    list.reverse(frase)
    frase = ' '.join(frase)
    frase = frase.rstrip()
    return frase