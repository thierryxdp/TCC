def inverte(frase):
    ''' Dada uma frase qualquer, retorna a frase
    onde todos os caracteres de pontuação, tenham
    sido substituídos por espaço.
    str -> str'''
    j = "!?,.:-;"
    for k in range(len(b)):
        frase = frase.replace(b[k]," ")
    fr = frase.lower()
    invert = fr.reverse()
    
    return invert