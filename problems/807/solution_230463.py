n1 = 0

def conta_frases(frase):
    n1 += str.count(frase,"!")
    n1 += str.count(frase,"?")
    n1 += str.count(frase,"...")
    n1 += str.count(frase,".")
    return n1