def busca(setor,m):
    matriz = []
    for i in range(len(m)):
        if setor in m[i][2]:
                matriz.append(m[i][0])
                matriz.append(m[i][1])
                matriz.append(m[i][3])
    return matriz