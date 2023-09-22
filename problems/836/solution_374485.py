def busca(setor,m4):
    dados=[]
    for i in range(len(m4)):
        for j in range(len(m4[0])):
            if setor == m4[i][j]:
                dados=list.remove(dados+m4[i],setor)
    return dados