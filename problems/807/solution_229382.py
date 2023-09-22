def conta_frases(texto):
    """
    funcao que dado um texto, retorna o numero de frases. 
    """
 
    texto = str.split(texto)
    return len(texto)