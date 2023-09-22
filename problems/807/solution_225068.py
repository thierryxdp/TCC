def conta_frases(t):
    pontos = ["!","?","...","."]
    contagem_pontos = [s.count(t) for i in pontos]
    total = sum(contagem_pontos)
    return total