def busca(setor,matriz):
    ''''''
    dados=[]
    for lista in matriz:
        if setor in lista:
            dados=dados+[del lista[2]]
            
    return dados