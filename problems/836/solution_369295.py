def busca(nome,matriz):
    nomescomum=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
        if nome in matriz[i]:
            list.remove(matriz[i],nome)
            list.append(nomescomum,matriz[i])
    return nomescomum