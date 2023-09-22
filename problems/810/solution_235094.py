import re 

def inverte(frase):
    ''' funcao que reverte a orem das palavras em uma frase
str -> str'''
    frase.re = frase
    frase = frase.split (' ')
    frase.reverse()
    return str.join(' ', frase)