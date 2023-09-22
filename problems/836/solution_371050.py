def busca(setor,m):
    matriz = []
    for i in range(len(m)):
        if setor == (m[i][2]):
                matriz.append(m[i][:2]+matriz[i][-1])
    return matriz