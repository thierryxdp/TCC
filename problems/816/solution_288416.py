def maiores(ls, n):
    """Dada uma lista de números inteiros e um número inteiro n, retorna outra lista,
contendo todos os números da lista original maior que n, ordenados em ordem crescente.
Casos de teste:
maiores([1, 2, 3, 4, 5, 6, 7], 4) = [5, 6, 7]
maiores([1, 3, 4, 5, 6, 7, 9], 3) = [4, 5, 6, 7, 9]
"""
    r = []
    for e in ls: 
        if e > n:
            r.append(e)
    list.sort(r)
    return r