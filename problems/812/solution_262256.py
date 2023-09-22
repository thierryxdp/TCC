def retira_pontuacao(frase):
    """ Recebe a frase onde todos os caracteres de pontuação ' ,.;:?!' são removidos. String--> String"""
    frase=frase.replace(","," ")
    frase=frase.replace(";"," ")
    frase=frase.replace("."," ")
    frase=frase.replace(":"," ")
    frase=frase.replace("-"," ")
    frase=frase.replace("?"," ")
    frase=frase.replace("!"," ")
    frase=frase.replace("–"," ")
    return frase