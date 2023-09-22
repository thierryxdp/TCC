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
    
    frase=frase.lower()
    a=list(frase)
    a.reverse()
    a=str.join(" ",list)
    
    return a