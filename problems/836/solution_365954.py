def busca(setor,matriz):
    l1=[]
    for linha in matriz:
        if setor in linha:
            list.remove(linha,setor)
            list.append(l1,linha)
    return l1