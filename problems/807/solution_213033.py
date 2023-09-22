def conta_frases (texto):
    '''
    Retorna o valor de frases em
    um texto
    String -> int

    '''
	
    "..." = True
    
    if "...":
        return texto.count(".") + texto.count("!") + texto.count("?") - 2
    else:
        return texto.count(".") + texto.count("!") + texto.count("?")