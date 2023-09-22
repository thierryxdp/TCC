def conta_frases(texto):
    """ Dado um texto contar o numero de frases baseando-se no numero de pontuações """"
    pontos = [".","!","?"]
    reticencia = ["..."]
    contagem_pontos = [texto.count(i) for i in pontos and reticencia]
    total = sum(contagem_pontos)
    if ("..." and "." in texto):
        reticencia= ["..."]
        total -= (reticencia*3)
    return total