def busca(setor,matriz):
    ''''''
    dados=[]
    for lista in matriz:
        if setor in lista:
            dados=dados+lista
    return dados