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
    frase.split(" ")
    frase=frase.lower()
  
   
    return frase