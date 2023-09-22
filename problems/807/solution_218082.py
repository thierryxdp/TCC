""" Contar frases através da formação de uma lista com os pontos separados""""
def conta_frases(frase):
    tamanho1 = len(frase)
    """frase = frase.replace(".", "  ")"""
    frase = frase.replace("!", "  ")
    frase = frase.replace("...","  ")
    frase = frase.replace("?","  ")
    
    tamanho2= len(frase)
    
    final = tamanho2 - tamanho1 

    return final