def media_matriz (m):
    soma = 0.00
    for a in range(len(m)):
        for b in range(len(m[0])):
        	soma = soma + m[a][b]
    return round((soma)/len(m)/len(m[0]), 2)