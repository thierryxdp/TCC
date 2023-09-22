def busca(setor,matriz):
    dados=[]
    linha=len(matriz)   
    for i in range(linha):
        if setor in matriz[i][2]:
            list.append(dados,matriz[i])
    for l in range(len(dados)):
        del dados[l][2]
    return dado