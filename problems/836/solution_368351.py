def busca(setor,m):
    acumulador=[]
    for i in range(len(m)):
        if m[i][2]==setor:
            acumulador.append(m[i])
            del acumulador[-1]
    return acumulador