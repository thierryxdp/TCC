def uppCons(f):
    """Retorna uma frase com todas as suas consoantes em maisculas e os demais
    caracteres exatamente como estavam na frase original.
    str -> str"""
	vogais = "aeiouáéíóúãõâôûîê"
	vogais = vogais+vogais.upper()
	r = ""
	for i in range(len(f)):
		if f[i] not in vogais:
			r = r + f[i].upper()
		else:
			r = r + f[i]
	return r