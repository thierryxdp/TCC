def busca(nome,matriz):
    nomescomum=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if nome in matriz[i][j]:
                list.remove(matriz[i])
                nomescomum=nomescomum+[matriz[i]]
    return matriz[i]