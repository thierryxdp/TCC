def inverte(frase):
    '''função que inverte as palavras de uma dada lista 
    list -> list'''
    frase = frase.replace('!', ' ')
    frase = frase.replace('?', ' ')
    frase = frase.replace('-', ' ')
    frase = frase.replace('.', ' ')
    frase = frase.replace(':', ' ')
    frase = frase.replace(';', ' ')
    frase = frase.replace(',', ' ')
    frase = str.lower(frase)
    frase = frase.split(' ':0)
    list.reverse(frase)
    frase = ' '.join(frase)
    return frase