""" Contar frases através da formação de uma lista com os pontos separados""""
def conta_frases(frase):
    frase = frase.replace(".", " ")
    frase = frase.replace("!", " ")
    frase = frase.replace("..."," ")
    frase = frase.replace("?"," ")
    
    lista_frase = frase.split(" ")
   
    return lista_frase