def conta_frases(frases):
    textoFrase = frases.replace("!",".")
    textoFrase = textoFrase.replace("?",".")
    textoFrase = textoFrase.replace("...",".")
    cont = 0
    for i in range(len(textoFrase)):
        if (textoFrase[i] == "."):
            cont += 1       
	return cont