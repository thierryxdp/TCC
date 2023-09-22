def media_matriz (m):
    'dada uma matriz, retorna a média aritimética de todos seus elementos. str -> float'
    soma = 0.00
    for a in range(len(m)):
        for b in range(len(m[0])):
        	soma = soma + m[a][b]
    return round((soma)/len(m)/len(m[0]), 2)