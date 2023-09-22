def conta_frases(texto):
    """ Dado um texto contar o numero de frases baseando-se no numero de pontuações """"
    pontos = [".","!","?","..."]
    contagem_pontos = [texto.count(i) for i in pontos]
    total = sum(contagem_pontos)
    if ("..." and "." in texto):
        reticencia= ["..."]
        total -= (reticencia*3)
    return total