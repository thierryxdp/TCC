def inverte(frase):
    '''Esta funcao retorna uma frase na ordem inversa, sem letras maiusculas e sem pontuacao.'''
    '''str --> str'''
    frase = str.replace(frase, '.', '')
    frase = str.replace(frase, ',', '')
    frase = str.replace(frase, '-', ' ')
    frase = str.replace(frase, '?', '')
    frase = str.replace(frase, '!', '')
    frase = str.lower(frase)
    frase = str.split(frase, ' ')
    list.reverse(frase)
    frase = str.join(' ', frase)
    return frase