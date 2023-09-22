def retira_pontuacao(frase):
    ''' função que substitui todos os caracteres de pontuação e retorna todos eles substituidos por espaço
    str -> str
    '''
    frase=frase.replace("."," ")
    frase=frase.replace(";"," ")
    frase=frase.replace(","," ")
    frase=frase.replace(":"," ")
    frase=frase.replace("-"," ")
    frase=frase.replace("?"," ")
    frase=frase.replace("!"," ")
    return frase