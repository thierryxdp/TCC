def conta_numero(numero, matriz):
    """
    Função para contar quantas vezes um número está dentro de uma matriz.
    numero - é o número que se deseja buscar.
    matriz - é a matriz que se vai buscar o número.
    int, list(list) --> int
    """
    count = 0
    n_linha = len(matriz)
    if n_linha == 0:
        return count
    n_coluna = len(matriz[0])
    for i in range(n_linha):
        for j in range(n_coluna):
            if matriz[i][j] == numero:
                count += 1
    return count