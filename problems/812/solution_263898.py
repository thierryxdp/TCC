def retira_pontuacao(frase):
    """ Funçao que, dada uma frase,retorne a frase onde todos os caracteres de pontuação sejam substituidos por espaço"""
    frase=str.replace(frase,"-"," ")
    frase=str.replace(frase,","," ")
    frase=str.replace(frase,":"," ")
    frase=str.replace(frase,";"," ")
    frase=str.replace(frase,"."," ")
    frase=str.replace(frase,"!"," ")
    frase=str.replace(frase,"?"," ")
    return frase