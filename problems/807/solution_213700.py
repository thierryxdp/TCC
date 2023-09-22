def conta_frases(texto):
    """essa funcao, dada um texto do tipo str como parametro de entrada,
	 retorna o numero de frases contidas nele str -> int."""
    
    conta_excla = str.count(texto, "!")
    conta_ponto = str.count(texto, ".")
    conta_inter = str.count(texto, "?")
    conta_reti = str.count(texto, "...")
    
    if "..." in texto:
        frases = conta_excla + (conta_ponto - (3*conta_reti)) + conta_inter + conta_reti
        return frases
    else:
        frases = conta_excla + conta_ponto + conta_inter + conta_reti
        return frases