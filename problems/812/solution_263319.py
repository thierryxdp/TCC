def retira_pontuacao(frase):
	type(frase) == str
	if "-" in frase:
		frase= frase.replace("-"," ")
	if "," in frase:
		frase =frase.replace(","," ")
	if ":" in frase:
		frase = frase.replace(":"," ")
	if "." in frase:
		frase = frase.replace("."," ")
	if "!" in frase:
        frase = frase.replace("!"," ")
    if "?" in frase:
        frase = frase.replace("?"," ")
    return frase