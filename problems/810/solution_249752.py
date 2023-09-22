def inverte(frase):
    '''função que dada uma frase, substitui todos os caracteres de pontuação por espaço'''
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
    frase2 = ' '.join(frase1[0:len(frase1)+1])
    return frase2