def busca(setor,matriz):
    dados=[]
    for x in matriz:
        if setor==x[2]:
            dados.append([x[0],x[1],x[3]])
    return dados