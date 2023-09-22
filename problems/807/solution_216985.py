def conta_frases(texto : str)->int:
    """Dado um texto, retorna a quantidade de frases desse texto."""
    
    texto_limpo = str.replace(str.replace(str.replace(texto,'...','.'),'?','.'),'!','.')
    return len(str.split(texto_limpo,'.')