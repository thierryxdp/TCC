def inverte(frase):
    '''Retorna uma string com as mesmas palavras da frase inserida, mas na
    ordem inversa, sem letras maiúsculas e sem pontuação'''
    frase=str.lower(frase)
    frase=str.replace(frase, ', ', ' ')
    frase=str.replace(frase, '. ', ' ')
    frase=str.replace(frase, '.', '')
    frase=str.replace(frase, '-', ' ')
    frase=str.replace(frase, '!', '')
    frase=str.replace(frase, '?', '')
    frase=str.split(frase)
    list.reverse(frase)
    frase=str(frase)
    frase=str.replace(frase, "', '", ' ')
    frase=str.replace(frase, "['", '')
    frase=str.replace(frase, "']", '')
    return frase