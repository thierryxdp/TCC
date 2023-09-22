def conta_frases(texto):
    """funcao que retorna quantas frases um texto possui;
    str -> int"""
    frases = str.count(texto, ".") + str.count(texto, "!") + str.count(texto, "?")
    if "..." in texto:
        return frases - 2
	return frases