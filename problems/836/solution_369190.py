def busca(nome,matriz):
    nomescomum=[]
    for i in range(len(matriz)):
        list.append(nomescomum,nome)
        for j in range(len(matriz[0])):
            if nome in matriz[i][j]:
                list.remove(matriz[i][j],nome)
    return nomescomum