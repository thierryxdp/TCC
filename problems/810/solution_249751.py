def inverte(frase):
    '''função que dada uma frase, substitui todos os caracteres de pontuação por espaço, inverte a ordem da frase e tira as letras maiúsculas'''
    frase = str.lower(frase)
    frase = str.replace(frase, '.', '')
    frase = str.replace(frase, ',', '')
    frase = str.replace(frase, ';', '')
    frase = str.replace(frase, '-', '')
    frase = str.replace(frase, '?', '')
    frase = str.replace(frase, '!', '')
    frase = str.replace(frase, '...', '')
    frase = str.replace(frase, ':', '')
    frase1 = str.split(frase, ' ')
    frase1.reverse()
    frase2 = ' '.join(frase1[:])
    return frase2