def conta_frases(frase):
    frase = str.split(frase, "!")
    frase = str.join(".", frase)
        frase = str.split(frase, "?")
    frase = str.join(".", frase)
    #frase = str.strip(frase)
    frase = str.split(frase,".")
    x = len(frase)
    return(x-1)