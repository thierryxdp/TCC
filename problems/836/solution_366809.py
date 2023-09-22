def busca(area, matriz):
    dados = []
    for lin in range(0, len(matriz)):
        for col in range(0, len(matriz[lin])):
            if area.lower() == matriz[lin][col].lower():
                dados.append(matriz[lin])


    if area in dados[0] and area in dados[1]:
        dados[0].remove(area)
        dados[1].remove(area)
        
    return dados