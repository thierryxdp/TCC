def inverte(frase):
    ''' Dada uma frase qualquer, retorna a frase
    onde todos os caracteres de pontuação, tenham
    sido substituídos por espaço.
    str -> str'''
    j = "!?,.:-;"
    for k in range(len(j)):
        frase = frase.replace(j[k]," ")
    fr = frase.lower()
    invert = fr[::-1]
    
    return invert