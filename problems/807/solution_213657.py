def conta_frases(texto):
    """essa funcao, dada um texto do tipo str como parametro de entrada,
	 retorna o numero de frases contidas nele str -> int."""
    
    excla_limpa = str.split(texto, "!")
    inter_limpa = str.split(excla_limpa, "?")
    reti_limpa = str.split(inter_limpa, "...")
    
    return len(reti_limpa)