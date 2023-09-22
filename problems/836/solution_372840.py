def busca(setor,matriz):
    ''''''
    dados=[]
    for linha in matriz:
        if setor in matriz[0]:
            dados=dados+linha
    return dados