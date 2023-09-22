def inverte(frase):
    """Esta função recebe uma frase e inverte suas palavras
    str -> str"""
	frase = frase.replace("."," ")
	frase = frase.replace(","," ")
	frase = frase.replace("!"," ")
	frase = frase.replace("?"," ")
	frase = frase.replace("-"," ")
	frase = frase.replace("_"," ")
	frase = frase.lower()
    frase = str.split(frase)
    frase = frase[-1]
    frase = str.join(,frase)
    return frase