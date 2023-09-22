def conta_frases(frase):
    """calcula o numero de frases que aparecem no texto"""
    frase_sub=frase.replace("...","#").replace("?","#").replace("!","#").replace(".","#") 
    contagem=frase_sub.count("#")
    return contagem