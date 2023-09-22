def melhor_volta(matriz):
    menor = min(matriz[0])
    volta = 1
    for lista in matriz:
        if min(lista) <= menor:
            menor = min(lista)
            volta = matriz.index(lista) + 1
    return volta, menor, matriz[volta-1].index(menor)+1