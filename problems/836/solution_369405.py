def busca(setor,m):
    matriz=[]
    for  i in range(len(m)):
        if setor in m[i]:
            matriz.append(m[i][:2]+[m[i][3]]
    return matriz