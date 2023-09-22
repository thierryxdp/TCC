n1 = 0

def conta_frases(frase):
    n1 = str.count(frase,"!")
    n2 = str.count(frase,"?")
    n3 = str.count(frase,"...")
    n4 = str.count(frase,".")
    nt = n1 + n2 + n3 + n4
    return nt