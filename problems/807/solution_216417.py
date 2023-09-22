def conta_frases(frase):
    ret = '...'
    ponfinal = '.'
    x = frase.split(ponfinal)+frase.split(ret)+frase.split("!")+frase.split("?")
    return len(x)