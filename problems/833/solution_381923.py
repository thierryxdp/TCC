def conta_numero(numero,matriz):
    """Retorna quantas vezes um número aparece na matriz; int, list -> int."""
    x = 0
    for i in range(0,len(matriz)):
        for j in range(0, len(matriz[i])):
            if numero == matriz[i][j]:
                x += 1
    return x