def busca(setor,m4):
    dados=[]
    for i in range(len(m4)):
        for j in range(len(m4[0])):
            if setor == m4[i][j]:
                
                dados=dados+m4[i],setor
                for i in range(len(dados)):
                    for j in range(len(dados)):
                        if setor in dados[i][j]:
                            list.remove(dados,setor)
    return dados