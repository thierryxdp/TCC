def conta_frase(frase):
    frase = str.split(frase,".")
    frase = str.split(frase,"!")
    frase = str.split(frase,"?")
    frase = str.split(frase,"...")
    return len(frase)