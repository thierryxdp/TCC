def conta_frases(s):
    pontos = [".","!","?","..."]
    contagem_pontos = [s.count(i) for i in pontos]
    if ('...' in s and '.' in s):
        total = sum(contagem_pontos)-3
        return total
    else:
        total = sum(contagem_pontos)
        return total