def maiores (listaNum, n):
   '''Função que recebe uma lista de números e inteiros e um inteiro n
    e que retorna nova lista com todos os numeros maiores que n,
    em ordme crescente
    list, int => list''''
    maiores=list()
    listaNum.sort()
    for c in listaNum:
    if c >= n:
        maiores.append(c)
    return maiores