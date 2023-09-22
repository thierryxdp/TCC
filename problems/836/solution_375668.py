def busca(setor, matriz):
    dados = []
    for i in range(len(matriz)):
        if setor in matriz[i]:
            dados.append(matriz[i])
            or j in range(len(dados)):
                if dados[j][2] == setor:
                    del dados[j][2]