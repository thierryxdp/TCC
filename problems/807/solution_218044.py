""" Contar frases através da formação de uma lista com os pontos separados""""
def conta_frases(frase):
    frase = frase.replace(".", " ")
    frase = frase.replace("!", " ")
    frase = frase.replace("..."," ")
    frase = frase.replace("?"," ")
    
   
    return frase