def insere(lista_numero, n):
    """Recebe como parâmetro uma lista crescente de números inteiros e um número inteiro n e retorna a lista inicial acrescida do núero n de tal forma que a lista permanece ordenada;
    assinatura: list[...], n --> list[...]
    Casos de teste:
    insere([1, 2, 3, 5], 4) == [1, 2, 3, 4, 5]
    insere([1, 2, 3, 4, 7, 9], 6) == [1, 2, 3, 4, 6, 7, 9]
    insere([-5, 0, 32,40], -2) == [-5, -2, 0, 32, 40]
    """
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero