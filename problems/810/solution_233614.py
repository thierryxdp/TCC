def inverte(frase):
    '''dada uma frase, retorna outra com as palavras na ordem inversa
    str -> str'''
    frase = str.lower (frase)
    str.replace (frase, '-', ' ')
    str.replace (frase, '.', ' ')
    str.replace (frase, '!', ' ')
    str.replace (frase, '?', ' ')
    return str.split (frase, ' ', -1, 0, -1)