def conta_numero(numero,matriz):
    """A função recebe um numero inteiro e uma matriz de inteiros,
    e retorna quantas vezes o numero aparece dentro da matriz;
    int, list(list) -> int"""
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if numero == matriz[i][j]:
                soma += 1
    return soma