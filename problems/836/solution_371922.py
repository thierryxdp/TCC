def busca(area, matriz):
    for i in range(len(matriz)):
        for counter in range(len(matriz)):
            for counter2 in range(len(matriz)):
                if counter2 == area:
                    return matriz[i]