def conta_frases (texto):
    '''
    Retorna o valor de frases em
    um texto
    String -> int

    '''
	  
     if texto.count("...") < 1:
        return texto.count(".") + texto.count("!") + texto.count("?")
    
    elif texto.count("...") == 1:
        return texto.count(".") + texto.count("!") + texto.count("?") - 3
    
    else texto.count("...") == 2:
        return texto.count(".") + texto.count("!") + texto.count("?") - 6