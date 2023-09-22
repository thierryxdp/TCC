def busca(nome,matriz):
    nomescomum=[]
    for i in range(len(matriz)):
        list.remove(nomescomum[i],nome)
        for j in range(len(matriz[0])):
            if nome in matriz[i][j]:
                nomescomum=nomescomum+[matriz[i]]
    return nomescomum