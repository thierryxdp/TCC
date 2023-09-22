def media_matriz(matriz):
    "Função que recebe uma matriz de inteiros, não vazia, e retorna a média de todos os seus números."
    "list -> float"
    soma = []
    for lin in matriz:
        for inteiros in lin:
            soma += [inteiros]
    return round(sum(soma)/(len(matriz)*len(matriz[0])),2)