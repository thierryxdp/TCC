def inverte(frase):
    frase = remove_punctuation(frase)
    frase = frase.lower()
    frase = frase.split()
    frase.reverse()
    frase = " ".join(frase)
    
    return(frase)