def busca(setor,matriz):
    ''''''
    dados=[]
    for lista in matriz:
        if setor in lista:
            dados=dados+list.remove(lista,setor)
            
    return dados