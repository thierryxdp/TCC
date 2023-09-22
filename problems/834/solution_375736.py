def media_matriz(matriz):
    """Esta é a funão que dada uma matriz de inteiros não vazia, retorna a média de todos os números da matriz com duas casas de precisão; list -> float"""
    elementos = []

    for l in range(len(matriz)):
        for c in range(len(matriz[l])):

            if matriz[l][c] != 0:
                list.append(elementos,matriz[l][c])

    return round(sum(elementos)/len(elementos),2)