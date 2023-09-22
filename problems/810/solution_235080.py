def inverte(frase):
    ''' funcao que reverte a ordem das palavras em uma frase
str -> str'''
    fras = frase.split (' ')
    return str.join(' ', fras)