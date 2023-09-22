def conta_frases(texto):
    contador1 = 0
    contador2 = 0
    contador3 = 0
    contador4 = 0
    contador1 = len(texto.split("."))-1
    contador2 = len(texto.split('!'))-1
    contador3 = len(texto.split('?'))-1
    contador4 = len(texto.split("..."))-1
    return contador1+contador2+contador3+contador4