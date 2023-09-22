def inverte(frase):
    frase=str.replace(frase, ".", " ")
    frase=str.replace(frase, "...", " ")
    frase=str.replace(frase, "-", " ")
    frase=str.replace(frase, ";", " ")
    frase=str.replace(frase, "!", " ")
    frase=str.replace(frase, ":", " ")
    frase=str.replace(frase, "?", " ")
	frase=str.replace(frase, ",", " ")
    frase = frase(reverse=True)
    return frase