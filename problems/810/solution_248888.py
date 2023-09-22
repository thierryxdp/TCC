def inverte(frase):
    '''Retorna uma frase contendo as mesmas palavras de ordem inversa, sem letras maiusculas,
    e sem pontuação.'''
    frase = str.replace(frase, '!','')
    frase = str.replace(frase, '.','')
    frase = str.replace(frase, '?','')
    frase = str.replace(frase, ',','')
    frase = str.lower(frase)
    list.reverse(frase)
    frase = str.join(' ',frase)
    return frase