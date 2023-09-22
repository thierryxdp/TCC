def n_frases (texto:str) -> int:
    """Função que irá contar o número de frases de um texto.
    
    	Parameters:
        texto: texto que deverá ser analisado
        
        Returns:
        número de frases do texto inserido
    """

    return str.count(texto, ".") + str.count(texto, "!") + str.count(texto, "?") + str.count(texto, "...")