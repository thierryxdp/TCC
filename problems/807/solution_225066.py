def conta_frases(s):
    pontos = ["!","?","...","."]
    contagem_pontos = [s.count(i) for i in pontos]
    total = sum(contagem_pontos)
    return total