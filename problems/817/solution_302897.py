def maiores(ls, n):
    """Dada uma lista de números inteiros e um número inteiro n, retorna outra lista,
contendo todos os números da lista original maior que n, ordenados em ordem crescente.
Assinatura: list, int -> list
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

def acima_da_media(ls):
    """Dada uma lista com notas de alunos de uma turma, retorna uma lista ordenada com 
as notas que ficaram acima da média.
Assinatura: list -> list
Casos de teste:
acima_da_media([3, 5, 6, 7]) = [6, 7]
acima_da_media([1, 2, 6, 8]) = [6, 8]
"""
    nt = len(ls)
    soma_nt = sum(ls)
    md = soma_nt / nt
    return maiores(ls, md)