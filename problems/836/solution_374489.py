def busca(setor,m4):
    dados=[]
    for i in range(len(m4)):
        for j in range(len(m4[0])):
            if setor == m4[i][j]:
                dados=dados+m4[i],setor
                
            if setor == m4[i][j]:
                list.del(dados[i][j])
                
            
    return dados