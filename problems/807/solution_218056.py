""" Contar frases através da formação de uma lista com os pontos separados""""
def conta_frases(frase):
    frase = frase.split(".")
    frase = frase.split("!")
    frase = frase.split("...")
    frase = frase.split("?")
    
    
   
    return frase