def conta_frases(frases):
    textoFrase = frases.replace("!",".")
    textoFrase = frases.replace("?",".")
    textoFrase = frases.replace("...",".")
    cont = 0
    for i in range(len(frases)-1):
        if (frases[i] == "."):
            cont += 1       
	return frases