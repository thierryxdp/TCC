def conta_frases(frase):
    ponto = '.'
    reticencias = '..'
    x = frase.count(ponto)+frase.count(reticencias)+frase.count("!")+frase.count("?")
    return (x)