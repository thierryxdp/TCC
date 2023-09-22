def maiores(lis, n):
    maiores_numeros = list()
    numeros = [int(numero) for numero in numeros]
    numeros.sort()  # Crescente
    for c in lis:
        if c >= n:
            maiores_numeros.append(c)
    return maiores_numeros