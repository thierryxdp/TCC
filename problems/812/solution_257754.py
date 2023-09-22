def retira_pontuacao(frase):
    """ Dada uma frase, retorna sem nenhuma pontuação. string>string"""
    frase = frase.replace("!"," ")
    frase = frase.replace("."," ")
    frase = frase.replace(":"," ")
    frase = frase.replace("?"," ")
    frase = frase.replace(","," ")
    frase = frase.replace("-"," ")
    frase = frase.replace(";"," ")
    return frase