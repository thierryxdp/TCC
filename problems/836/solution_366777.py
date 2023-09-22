def busca(area, matriz):
    dados = []
    for lin in range(0, len(matriz)):
        for col in range(0, len(matriz[lin])):
            if area.lower() == matriz[lin][col].lower():
                dados = matriz[lin].copy()
                dados.remove(area)

    return [dados]