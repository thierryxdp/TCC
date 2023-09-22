def conta_frases(frase):
    n1 = str.count(frase,"!")
    n1 += str.count(texto,"?")
    n1 += str.count(texto,"...") - 3
    n1 += str.count(texto,".")
    return n1