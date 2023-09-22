def maiores(lista_numero, n):
    """Recebe como parâmetro uma lista de números inteiros e um número inteiro n e retorna outra lista contendo todos os números da lista original maiores que n, em ordem crescente;
    assinatura: list[...], int --> list[...]
    Casos de teste:
    maiores([1, 2, 3, 4], 2) == [3, 4]
    maiores([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    maiores([-7, -6, -5, -4], -6) == [-5, -4]
    """
    lista_numero.sort(reverse = True)
    lista_aux = []
    for e in lista_numero:
        if e > n:
            lista_aux.append(e)
    lista_aux.sort()
    return lista_aux

def acima_da_media(l):
    """Recebe uma lista com as notas dos alunos de uma turma e retorna uma lista ordenada com as notas que ficaram acima da média;
	assinatura: list[...] --> list[...]
    Casos de teste:
    acima_da_media([5, 6, 7, 9, 10, 8, 5, 6]) == [8, 9, 10]
    acima_da_media([3, 4, 5, 5, 2, 1.5, 2]) == [4, 5, 5]
    """
    media = sum(l) / len(l)
    l1 = maiores(l, media)
    return l1