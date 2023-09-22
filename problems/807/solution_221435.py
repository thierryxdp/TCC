def conta_frases(frase):
    """ 
    Função que dada uma str, retorna a quantidade de frases 
    que aparecem no texto. 
    str-> int
    """
    return len(frase.replace('.','!','?','...','.'))str.split