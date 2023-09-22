def busca(setor,matriz):
    ''''''
    
    
    dados=[]
    for i in matriz:
        if setor not in matriz:
            dados=dados+matriz
    return dados