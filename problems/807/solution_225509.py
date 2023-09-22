def conta_frases(texto):
    """ Dado um texto contar o numero de frases baseando-se no numero de pontuações """"
    pontos1 = [".","!","?","..."]
    contagem_pontos = [texto.count(i) for i in pontos1]
    total = sum(contagem_pontos)
    return total