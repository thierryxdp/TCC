def conta_frases(string):
    pontuacao = ["!", "?", "...", "."]
    conta_pont = [string.count(i) for i in pontuacao]
    conta_pont[3] -= conta_pont[2] * 3
    total = sum(conta_pont)
    return total