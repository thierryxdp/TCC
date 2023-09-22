def media_matriz (m):
    soma = 0.00
    a = 0
    b = 0
    for a in len(m):
        for b in len(m[0]):
        	soma = soma + int(m[a][b])
    return soma