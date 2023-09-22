def busca(setor,matriz):
    ''''''
    dados=[]
    for lista in matriz:
        if setor in lista:
            list.remove(lista,2)
            dados=dados+[lista]
    return dados