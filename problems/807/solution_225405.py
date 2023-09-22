def conta_frases(s):
    pontos = [".","!","?","..."]
    contagem_pontos = [s.count(i) for i in pontos]
    if ('...' in s and '.' in s):
        total = sum(contagem_pontos)-3
        return total
    elif s.count('...')>=2:
        total = sum(contagem_pontos)-3*s.count('...')
        return total
    else:
        total = sum(contagem_pontos)
        return total