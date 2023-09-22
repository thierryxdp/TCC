def conta_numero (n, matriz):
    'dado um numero inteiro e uma matriz, retorna quantas vezes o numero aparece na matriz. int, str -> int'
    count = 0
    for a in range(len(matriz)):
        for b in len(matriz[c]):
            if b == n:
                count = count + 1
                c += 1
    return count