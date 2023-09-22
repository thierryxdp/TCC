def conta_frases(texto):

	frase = texto.replace("?", ".")
    frase2 = frase.replace("!", ".")
    frase3 = frase2.replace("...", ".")
    
    cont = frase3.split(".")
    cont = len(cont)
        
    
    return cont