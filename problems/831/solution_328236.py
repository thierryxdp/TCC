def lingua_p(palavra):
    """Função que recebe uma palavra e retorna ela traduzida para
    a lingua do p"""
    p = str.lower(palavra)
    r = ""
    for i in range(0, len(p)):
        if p[i] not in "aeiouáéú":
            r = r + p[i]
		if p[i] in "aeiouáéú":
            r = r + p[i] + "p" + p[i] 
	return r