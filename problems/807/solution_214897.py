def conta_frases(frases):
    """ função que dado um texto, conte o numero de frases que a nesse texto.
    Levando em consideração que as frases terminam com ponto final, ponto de exclamação,
    ponto de interrogação ou com reticências
    str --> int"""
    texto = frase.replace("." , " ")
    texto = frase.replace("!" , " ")
    texto = frase.replace("?" , " ")
    texto = frase.replace("..." , "  ")
    contar = len(texto)
    return contar