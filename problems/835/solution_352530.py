def melhor_volta(mat):
    corredores = [1, 2, 3, 4, 5, 6]
    voltas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    matrix = [for x in range(6) for y in range(10)]
    faster = []
    proximo = 0
    for linha in matrix:
        for coluna in matrix:
            proximo = proximo +1
            faster = min(matrix)

    return (faster, corredores, voltas)