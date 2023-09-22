def conta_frases(texto):

	frase = texto.replace("?", ".")
    frase = texto.replace("!", ".")
    frase = frase.replace("...", ".")
    
    cont = frase.split(".")
    cont = len(cont)
        
    
    return cont