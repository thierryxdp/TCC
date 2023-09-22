def inverte(frase):
    frase = frase.retirapontuacao (frase)
    frase = frase.lower()
    frase = frase.split()
    frase.reverse()
    frase = " ".join(frase)
    
    return(frase)