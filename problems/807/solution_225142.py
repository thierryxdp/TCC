def conta_frases(s):
    pontos = ["!", "?", "...", "."]
    contagem = [s.count(i) for i in pontos]
    contagem[3] -= contagem[2] * 3
    total = sum(contagem)
    return total