def maiores(lis, n):
    'Funçao que retorna os numeros maiores que n em ordem crescente'
    maiores_numeros = list()
    for c in lis:
        if c < n:
            maiores_numeros.append(c)
    return maiores_numeros