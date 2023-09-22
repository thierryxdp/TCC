import re 

def inverte(frase):
    ''' funcao que reverte a ordem das palavras em uma frase
str -> str'''
    frases = ['.',',','!']
    frase = frase.split (' ')
    for c in frase:
        frase = frases.replace(c, '')
    return (frase)