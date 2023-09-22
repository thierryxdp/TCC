def busca(string, matriz):
    dados = []
    for i in range(len(matriz)):
        if string == matriz[i][2]:
            dados += [matriz[i][0], matriz[i][1], matriz[i][3]]
    return dados