n1 = 0

def conta_frases(frase):
    n1 = str.count(frase,"!")
    n1 += str.count(frase,"?")
    if (str.count(frase,"...") > 0):
    	n1 += str.count(frase,"...") - 3*str.count(frase,"...")
    n1 += str.count(frase,".")
    return n1