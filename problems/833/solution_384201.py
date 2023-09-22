def conta_numero(numero: int, matriz: list) -> int:
    """Retorna quantas vezes o número aparece na matriz"""
    
    contador = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == numero:
                contador = contador + 1
    return contador