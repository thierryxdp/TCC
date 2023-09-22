import re 

def inverte(frase):
    ''' funcao que reverte a ordem das palavras em uma frase
str -> str'''
    
    frase = frase.split (' ')
    for frases in frase:
        frase = frase.replace(frases, " ")
    return (frase)