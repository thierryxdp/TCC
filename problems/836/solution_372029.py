def busca(string, matriz):
    dados = []
    string = ''
    for i in range(len(matriz)):
        if string in matriz[i][2]:
            dados += [matriz[i][0], matriz[i][1], matriz[i][3]]
        else:
            dados = []
    return dados