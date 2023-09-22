def busca(setor,m4):
    dados=[]
    for i in range(len(m4)):
        for j in range(len(m4[0])):
            if setor == m4[i][j]:
                
                dados=dados+m4[i]
                for i in range(len(dados)):
                    for j in range(len(dados)):
                        if setor == dados[i][j]:
                            dados.remove(setor)
    return dados