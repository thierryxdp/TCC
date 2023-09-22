def retira_pontuacao(frase):
    '''função que retorna uma frase sem pontuação'''
    '''str->str'''
    frase=frase.replace("."," ")
    frase=frase.replace("/"," ")
    frase=frase.replace(";"," ")
    frase=frase.replace(","," ")
    frase=frase.replace(":"," ")
    frase=frase.replace("?"," ")
    frase=frase.replace("!"," ")
    frase=frase.replace("-"," ")