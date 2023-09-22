def inverte(frase):
    """Esta função recebe uma frase e inverte suas palavras
    str -> str"""
	frase = frase.replace("."," ")
	frase = frase.replace(","," ")
	frase = frase.replace("!"," ")
	frase = frase.replace("?"," ")
	frase = frase.replace("-"," ")
	frase = frase.replace("_"," ")
	frase = frase.lower( )
    frase = frase.split( )
    frase = frase[-1:]
    frase = frase.join( )
    return frase