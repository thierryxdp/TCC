def busca(m, setor):
    encontra = []
    for i in range(len(m)):
        if str(setor) in m[i]:
                encontra.append(m[i][0])
                encontra.append(m[i][1])
                encontra.append(m[i][3])
                    
    return encontra