def conta_frases(frase):
   
    y= frase.count('...')
    x= frase.count(".","?")
    
    if '.' in frase and "?" in frase:
        return x