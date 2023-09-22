def busca(setor,matriz):
    ''''''
    dados=[]
    for lista in matriz:
        if setor in lista:
            del lista[2]
            dados=dados+[lista]
    
    return dados