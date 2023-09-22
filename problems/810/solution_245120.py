def retira_pontuacao(frase):
     '''a funcao retorna uma frase sem pontuacao'''
    '''str->str'''
    frase=frase.replace("."," ")
    frase=frase.replace("/"," ")
    frase=frase.replace(";"," ")
    frase=frase.replace(","," ")
    frase=frase.replace(":"," ")
    frase=frase.replace("?"," ")
    frase=frase.replace("!"," ")
    frase=frase.replace("-"," ")
    return frase
def inverte(frase):
    palavras=frases.split()
    palavras=list(reversed(palavras))
    return" ", join(palavras))