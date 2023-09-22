# retorna a quantidade de frases de uma string, removendo os pontos especiais
def conta_frases(texto):
    total = 0
    for i in range(len(texto)):
        if i > 0 and texto[i - 1] == ".":
            continue
        if texto[i] in (".", "?", "!"):
            total += 1
    return total