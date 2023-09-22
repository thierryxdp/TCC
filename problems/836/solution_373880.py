def busca(m, setor):
    encontra = []
    for i in range(len(m)):
        if setor in m[i]:
            for j in range(len(m[0])):
                if  m[i][j] != setor:
                    list.append(encontra, m[i][j])
    return encontra