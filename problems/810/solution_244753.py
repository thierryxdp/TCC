def retira_pontuacao(frase):
    '''retorna frase sem pontuacao'''
    frase=frase.replace("."," ")
    frase=frase.replace("/"," ")
    frase=frase.replace(";"," ")
    frase=frase.replace(","," ")
    frase=frase.replace(":"," ")
    frase=frase.replace("-"," ")
    frase=frase.replace("?"," ")
    frase=frase.replace("!"," ")
    return frase
def inverte(frase):
    '''retorna outra frase que contenha as mesmas palavras da frase de entrada na ordem inversa'''
    return frase[::-1]