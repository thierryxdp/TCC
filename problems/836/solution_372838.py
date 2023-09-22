def busca(setor,matriz):
    ''''''
    dados=0
    for linha in matriz:
        if setor in matriz:
            dados=dados+linha
    return dados