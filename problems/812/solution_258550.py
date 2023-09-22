def retira_pontuacao (frase):
    '''função que retira a pontução de qualqur frase'''
    ''' str -> str'''
    frase = frase.replace("!",".")
    frase = frase.replace("...",".")
    frase = frase.replace("?",".")
    frase = frase.split(".")
    frase
    return len(frase)-1