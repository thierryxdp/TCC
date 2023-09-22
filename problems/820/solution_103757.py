def posLetra(texto, letra, posicao):
    """docs"""
    
    a = len(texto)
    b = str.index(texto, letra)
    c = str.index(texto, letra)
    i = 0
    x = 0
    
    if 1 == posicao:
        return b
    elif c < posicao:
        return -1
    
    while i < a:
        i += 1
        x = x + 1
	return i