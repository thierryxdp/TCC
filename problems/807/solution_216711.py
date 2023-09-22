def conta_frases(frase):
    ponto = '.'
    ret = '.. '
    x = frase.count(ponto)+frase.count(ret)+frase.count("!")+frase.count("?")
    return (x)