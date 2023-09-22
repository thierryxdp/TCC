def conta_frases(texto):
    """
    	Retorna o número de frases em dado texto
    	str -> int
    """
    text = texto
    
    return len(str.split(str.replace(str.replace(str.replace(texto,'?','.'),'!','.'),'...','.'),'.'))-1