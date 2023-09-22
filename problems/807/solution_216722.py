def conta_frases(frase):
    ponto = '.'
    if frase.endswith('..'):
        return (x-2)
    else:
        x = frase.count(ponto)+frase.count("!")+frase.count("?")
        return (x)