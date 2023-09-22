def busca(setor,m):
    matriz_setor = []
    for i in range(len(m)):
        if m[i][2] == setor:
            info = m[i][0] + m[i][1] + m[i][3]
            list.append(matriz_setor,info)
    return matriz_setor