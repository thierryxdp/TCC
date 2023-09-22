def conta_frases(s):
    pontos = [".","!","?","..."]
    contagem_pontos = [s.count(i) for i in pontos]
    contagem_pontos[3] -= contagem_pontos[2] * 3
    total = sum(contagem_pontos)
    return total