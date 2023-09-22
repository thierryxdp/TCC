def busca(setor,matriz):
    nlinhas = len(matriz)
    ncolunas = len(matriz[0])
    linha = []
    for i in range(nlinhas):
        for j in range(ncolunas):
            if setor == matriz[i][j]:
                linha.append(matriz[i][0])
                linha.append(matriz[i][1])
                linha.append(matriz[i][3])
    return linha