def busca(area, matriz):
    final = []
    for x in range(len(matriz)):
        if(matriz[x][2] == area):
            func = matriz[x][2]
            func.remove(area)
            final.append(func)
    return final