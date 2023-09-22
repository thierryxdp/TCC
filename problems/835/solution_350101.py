def melhor_volta(m):
    menor = m[0][1]
    linha = 0
    coluna = 0
    for j in range(10):
        for i in range(6):
            if m[i][1] < menor:
                menor = m[i][j]
                linha = i
                coluna = j
    return (linha+1, menor, coluna+1)