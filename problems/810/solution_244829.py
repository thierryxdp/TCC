def inverte(frase):
    """ Recebe a frase onde todos os caracteres de pontuação ' ,.;:?!' são removidos. String--> String"""
    frase=frase.replace(","," ")
    frase=frase.replace(";"," ")
    frase=frase.replace("."," ")
    frase=frase.replace(":"," ")
    frase=frase.replace("-"," ")
    frase=frase.replace("?"," ")
    frase=frase.replace("!"," ")
    frase=frase.replace("–"," ")
    frase=lower(frase)
    return frase[::-1]