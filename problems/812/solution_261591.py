def retira_pontuacao (frase):
    '''a funcao retorna uma frase sem pontuacao	'''
    '''str->str'''
    frase=frase.replace("."," ")
    frase=frase.replace("/"," ")
    frase=frase.replace(";"," ")
    frase=frase.replace(","," ")
    frase=frase.replace(":"," ")
    frase=frase.replace("?"," ")
    frase=frase.replace("!"," ")
    frase=frase.replace("_"," ")
    return frase