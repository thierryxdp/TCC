def busca(setor,m):
    acumulador=[]
    for i in range(len(m)):
        if m[i][1]==setor:
            acumulador.append(m[i])
    return acumulador