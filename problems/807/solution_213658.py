def conta_frases(texto):
    """essa funcao, dada um texto do tipo str como parametro de entrada,
	 retorna o numero de frases contidas nele str -> int."""
    
    texto_excla = str.split(texto, "!")
    texto_inter = str(texto_excla)
    texto_interro = str.split(texto_inter, "?")
    texto_re = str(texto_interro)
    texto_reti = str(texto_re)
    
    
    return len(texto_reti)