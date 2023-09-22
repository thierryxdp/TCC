def conta_frases(frase):
    ponto = '.'
    x = frase.count(ponto)+frase.count('.. ')+frase.count("!")+frase.count("?")
    return (x)