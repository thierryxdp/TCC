def busca(nome,matriz):
    contato = []
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if nome in matriz[i][j]:
                contato.append(matriz[i][i])
    return contato