def busca(setor,m):
    matriz=[]
    for  i in range(4):
        if setor in m[2]:
            matriz.append(m[i])
    return matriz