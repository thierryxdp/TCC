def conta_frases(frase):
	fraseMod=frase.replace("...","fraseDer").replace("!","fraseDer").replace("?","fraseDer").replace(".","fraseDer")
	return fraseMod.count("fraseDer")