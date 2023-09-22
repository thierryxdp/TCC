def busca(setor,matriz):
    ''''''
    dados=[]
    for linha in matriz:
        if setor in matriz:
            dados=dados+linha
    return dados