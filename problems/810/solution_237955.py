def inverte(frase):
    frase = frase.replace("."," ")
	frase = frase.replace(","," ")
	frase = frase.replace("!"," ")
	frase = frase.replace("?"," ")
	frase = frase.replace("-"," ")
	frase = frase.replace("_"," ")
    frase = frase.split( )
    frase = frase[-1] + frase[:-1]
    frase = frase.join()
    return frase