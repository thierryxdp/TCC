def media_matriz(matriz):
    """Esta é a funão que dada uma matriz de inteiros não vazia, retorna a média de todos os números da matriz com duas casas de precisão; list -> float"""
    elementos = []
    qtd_elementos = 0

    for l in range(len(matriz)):
        for c in range(len(matriz[l])):

            if matriz[l][c] != 0:
                list.append(elementos,matriz[l][c])
                qtd_elementos = qtd_elementos + 1

            else:
                qtd_elementos = qtd_elementos + 1

    return round(sum(elementos)/qtd_elementos,2)