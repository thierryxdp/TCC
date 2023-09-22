def busca(area, matriz):
    final = []
    for x in range(len(matriz)):
        if(matriz[x][2] == area):
            final.append(matriz[x])
    return final