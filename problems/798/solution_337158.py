def freq_palavras(frases):
    
	dicio = dict()
    frase_list = frases.split()
    frase_unique = set(frase_list)
    for palavra in frase_unique:
        dicio[palavra] = frase_list.count(“palavra”)
	
		
	return dicio