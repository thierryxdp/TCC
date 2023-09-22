def conta_frases(frases):
    textoFrase = frases.replace("!",".")
    textoFrase = frases.replace("?",".")
    textoFrase = frases.replace("...",".")
    cont = 0
    for i in range(len(textoFrase)-1):
        if (textoFrase[i] == "."):
            cont += 1       
	return cont