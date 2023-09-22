def busca(area,  matriz):
    resultado = []
    for i in range(0, len(matriz)):
        for j in range(0, len(matriz[i])):
            if area.lower() == matriz[i][j].lower():
                dados = matriz[i].copy()
                dados.pop(dados.index(dados[j]))
                resultado.append(dados)

    return resultado