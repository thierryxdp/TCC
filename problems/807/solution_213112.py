def conta_frases (texto):
    '''
    Retorna o valor de frases em
    um texto
    String -> int

    '''
	  
    if texto.count("...") == 1:
        return texto.count(".") + texto.count("!") + texto.count("?") - 2
    
    elif texto.count("...") == 2:
        return texto.count(".") + texto.count("!") + texto.count("?") - 4
    
    elif texto.count("...") == 3:
        return texto.count(".") + texto.count("!") + texto.count("?") - 6
    
    else:
        return texto.count(".") + texto.count("!") + texto.count("?")