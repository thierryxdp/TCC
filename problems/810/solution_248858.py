def inverte(frase):
    '''Retorna uma frase contendo as mesmas palavras de ordem inversa, sem letras maiusculas,
    e sem pontuação.
    frase->str'''
    frase = frase.replace('!',' ')
    frase = frase.replace('.',' ')
    frase = frase.replace('?',' ')
    frase = frase.replace(',',' ')
    frase = frase.lower(frase)
    list.reverse(frase)
    return frase