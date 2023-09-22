def inverte(frase):
    frase = frase.punctuation()
    frase = frase.lower()
    frase = frase.split()
    frase.reverse()
    frase = " ".join(frase)
    
    return(frase)