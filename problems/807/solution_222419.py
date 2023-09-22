def conta_frases(texto):
    #Função que conta quantas frases há em um texto
    #str -> int
    if texto.count("...") == 0:
    	total = texto.count(".")+texto.count("!")+texto.count("?")+texto.count("...")
	else:
        total = texto.count(".")+texto.count("!")+texto.count("?")-texto.count("...")
    return total