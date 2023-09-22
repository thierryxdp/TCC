def busca(setor,m4):
    dados=[]
    for i in range(len(m4)):
        for j in range(len(m4[0])):
            if setor == j:
                dados=dados+m4[i]
    return dados