def conta_frases(texto):
    """essa funcao, dada um texto do tipo str como parametro de entrada,
	 retorna o numero de frases contidas nele str -> int."""
    
    
    if "!" in texto:
        conta_excla = str.count(texto, "!")
        if "." in texto:
            conta_ponto = str.count(texto, ".")
        if "?" in texto:
            conta_inter = str.count(texto, "?")
        if "..." in texto: 
            conta_reti = str.count(texto, "...")
            frases = conta_excla + conta_ponto + conta_inter + conta_reti
            return frases