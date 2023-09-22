def conta_frases(texto):
    """ Dado um texto contar o numero de frases baseando-se no numero de pontuações """"
    pontos1 = [".","!","?"]
    pontos2 = ["..."]
    contagem_pontos = [texto.count(i) for i in pontos1]
    reticencias = [texto.count(i) for i in pontos2]
    total = sum([contagem_pontos,reticencias])
    return total