def retira_pontuacao(frase):
    '''Retorna a frase sem os sinais de pontuacao
    str -> str'''
    frase=frase.replace("-"," ")
    frase=frase.replace(","," ")
    frase=frase.replace(":"," ")
    frase=frase.replace(";"," ")
    frase=frase.replace("."," ")
    return frase