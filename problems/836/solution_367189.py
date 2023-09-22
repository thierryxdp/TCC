def busca(setor,m):
    """-"""
    dados=[]
    for i in range(3):
        if setor==m[i][2]:
            dados=dados+[[[m[i][0]]+[m[i][1]]+[m[i][3]]]]
    return dados