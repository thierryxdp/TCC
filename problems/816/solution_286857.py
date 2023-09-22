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