def conta_frases(s):
    pontos = [".","!","?","..."]
    contagem_pontos = [s.count(i) for i in pontos]
    len([1 for i in s if i == '.'])
    total = sum(contagem_pontos)
    return total