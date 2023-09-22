def media_matriz (m):
    soma = 0.00
    for a in len(m):
        for b in len(m[0]):
        	soma = soma + m[a][b]
    return soma