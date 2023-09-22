def inverte(frase):
    '''Retorna uma frase contendo as mesmas palavras de ordem inversa, sem letras maiusculas,
    e sem pontuação.
    frase->str'''
    frase = frase.replace('!',' ')
    frase = frase.replace('.',' ')
    frase = frase.replace('?',' ')
    frase = frase.replace(',',' ')
    frase = str.lower(frase)
    list.reverse(frase)
    str.join(' ', frase)
    return frase