def conta_frases(texto):

	frase = texto.replace("?", ".")
    frase = frase.replace("!", ".")
    frase = frase.replace("...", ".")
    
    cont = frase.spli(".")
    cont = len(cont)
        
    
    return cont