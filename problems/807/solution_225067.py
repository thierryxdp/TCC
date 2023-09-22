def conta_frases(t):
    pontos = ["!","?","...","."]
    contagem_pontos = [s.count(t) for t in pontos]
    total = sum(contagem_pontos)
    return total