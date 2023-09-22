def conta_frases(frase):
    from math import ceil
    return ceil(str.count(frase,".")/3) + str.count(frase,"!") + str.count(frase,"?")