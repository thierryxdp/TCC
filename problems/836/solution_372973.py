def busca(setor,matriz):
    ''''''
    dados=[]
    for lista in matriz:
        del lista[2]
        if setor in lista:
            dados=dados+[lista]
    
    return dados