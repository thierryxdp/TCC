def busca(setor,matriz):
    dados=[]
    linha=len(matriz)
    coluna=len(matriz[0])
    for i in range(linha):
        if setor in matriz[i][2]:
            list.append(dados,matriz[i])
    return dados