def conta_frases(frase):
    frase=str.split(frase)
    frase=str.count(frase,".")
    frase=str.count(frase,"!")
    frase=str.count(frase,"?")
    return frase