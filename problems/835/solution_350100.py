def melhor_volta(m):
    menor = m[0][1]
    linha = 0
    coluna = 0
    for i in range(6):
        for j in range(10):
            if m[i][1] < menor:
                menor = m[i][1]
                linha = i
                coluna = j
    return (linha+1, menor, coluna+1)