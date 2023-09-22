def media_matriz(matriz):
    """Função que retorna a média de todos os números da matriz de inteiros
    não vazia. list -> float"""
    soma = 0
    total_elem = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            soma = soma + matriz[i][j]
            total_elem = total_elem + 1
    return round(soma/total_elem, 2)