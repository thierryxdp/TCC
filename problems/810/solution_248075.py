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
    list.reverse(frase)
    frase = frase.split(' ')
    frase = ' '.join(frase)
    return frase