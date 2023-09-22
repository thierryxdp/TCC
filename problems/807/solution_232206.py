def conta_frases(texto):
    """funcao que retorna quantas frases um texto possui;
    str -> int"""
	return str.count(texto, ". ") + str.count(texto, "!") + str.count(texto, "?") + str.count(texto, "...")