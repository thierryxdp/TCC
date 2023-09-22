def inverte(frase):
    ''' funcao que reverte a ordem das palavras em uma frase
str -> str'''
    frase = frase.split (' ')
    return str.join(' ', frase)