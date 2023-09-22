def busca(setor,matriz):
    ''''''
    
    i=0
    dados=[]
    for i in matriz:
        if setor not in matriz:
            dados=dados+matriz
    return dados