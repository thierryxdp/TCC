def conta_frases(texto):

	frase = texto.replace("?", ".")
    frase = cont.replace("!", ".")
    frase = cont.replace("...", ".")
    
    cont = frase.spli(".")
    cont = len(cont)
        
    
    return cont