def conta_frases(texto):
    """
    Faca uma funcao que dado um texto, conte o numero de frases do texto. 
    Considere que o texto pode ter espacos no inicio e no final.
    """
    #texto = str.strip(texto)
    texto = str.split(texto)
    return len(texto)