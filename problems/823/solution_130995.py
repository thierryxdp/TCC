def obi(n):
    """função que retorna o número inteiro que está faltando no intervalo de um a n na lista de entrada
    list -> int"""
    list.sort(n)
    indice = 0
    while indice < len(n):
        if n[0] != 1:
            return 1
        elif n[indice+1] != n[indice] + 1:
            return n[indice] + 1
        indice += 1