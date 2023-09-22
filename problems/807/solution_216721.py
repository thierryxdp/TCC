def conta_frases(frase):
    ponto = '.'
    x = frase.count(ponto)+frase.count("!")+frase.count("?")
    return (x)
    if frase.endswith('.'):
        return (x-2)