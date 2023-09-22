def busca(area, matriz):
    dados = []
    for lin in range(0, len(matriz)):
        for col in range(0, len(matriz[lin])):
            if area.lower() in matriz[lin][col].lower():
                dados = matriz[lin]

    dados.remove(area)
    return dados