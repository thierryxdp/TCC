def inverte(frase):
    for char in ".!?,":
        frase = frase.replace(char, "")
    
    return frase[ : :-1]