def maiores (numeros_int, n):
    '''Função que recebe uma lista de números e inteiros e um inteiro n
    e que retorna nova lista com todos os numeros maiores que n,
    em ordme crescente
    list, int => list''''
    maiores=list()
    numeros_int.sort()
    for c in numeros_int:
    if c >= n:
    maiores.append(c)
    return maiores