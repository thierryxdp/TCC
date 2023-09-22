def busca(area, matriz):
    dados = []
    for lin in range(0, len(matriz)):
        for col in range(0, len(matriz[lin])):
            if area.lower() == matriz[lin][col].lower():
                dados.append(matriz[lin])

    if len(dados) > 1:
        return dados

    else:
        return []