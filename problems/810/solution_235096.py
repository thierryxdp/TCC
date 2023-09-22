import re 

def inverte(frase):
    ''' funcao que reverte a ordem das palavras em uma frase
str -> str'''
    
    frase = frase.split (' ')
    frase.reverse()
    return str.join(' ', frase)