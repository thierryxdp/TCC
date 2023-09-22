def inverte(frase):
    """Esta função receba uma frase e inverte suas palavras
    str -> str"""
    frase = frase.replace("."," ")
	frase = frase.replace(","," ")
	frase = frase.replace("!"," ")
	frase = frase.replace("?"," ")
	frase = frase.replace("-"," ")
	frase = frase.replace("_"," ")
    frase = frase.lower( )
    frase = frase.split( )
    frase = frase[::-1]
    frase = str.join(" ",frase )
    return frase