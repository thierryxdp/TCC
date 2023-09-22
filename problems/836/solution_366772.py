def busca(area, matriz):
    for lin in range(0, len(matriz)):
        for col in range(0, len(matriz[lin])):
            if area.lower() == matriz[lin][col].lower():
                return matriz[lin]

            else:
                return []