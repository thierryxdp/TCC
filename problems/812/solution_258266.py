def retira_pontuacao(frase):
    '''função que dada uma frase retorne a mesma sem todas as pontuações, substituindo por espaço:
    srt -> srt'''
    frase.replace("."," ")
    frase.replace(","," ")
    frase.replace("?"," ")
    frase.replace("!"," ")
    frase.replace(":"," ")
    frase.replace(";"," ")
    return frase