def soma_h(N):
    """A função recebe como entrada um inteiro N e retona a
    soma 1 + 1/2 + 1/3 + 1/4 + ... + 1/N."""
    soma = 0
    lista = list(range(N + 1))
    del(lista[0])
    for numero in lista:
        soma += (1/numero)
    return soma