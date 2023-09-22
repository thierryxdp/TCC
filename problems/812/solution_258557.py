def retira_pontuacao (frase):
    '''função que retira a pontução de qualquer frase'''
    ''' str -> str'''
    frase = frase.replace("-"," ")
    frase
    frase = frase.replace("!"," ")
    frase = frase.replace("?"," ")
    frase
    frase = frase.replace(","," ")
    frase = frase.replace(":"," ")
    frase
    frase = frase.replace("."," ")
    return frase