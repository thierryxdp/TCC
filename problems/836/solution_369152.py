def busca(nome,matriz):
    nomescomum=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if nome in matriz[i][j]:
                nomescomum=nomescomum+matriz[j]
                list.remove(nomescomum,nome)
    return nomescomum