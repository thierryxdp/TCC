def conta_numero(numero,matriz):
    """Funçao que retorna a quantidade de vezes que um número inteiro aparece em uma matriz
int, list(list) -> int"""

    indice = 0
    total = 0

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            indice = indice + 1
            if matriz[i][j] == numero:
                total = total + 1
    return total