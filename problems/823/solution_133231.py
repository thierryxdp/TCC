def faltante(lista: list)-> int:
    """Dada uma lista com N-1 inteiros numerados de 1 a N, a função
    retorna o número inteiro deste intervalo está faltando"""
    i = 0
    listacerta = list(range(1, len(lista) + 2))
    while (i < len(lista)):
        if (lista[i] != listacerta[i]):
            return i + 1
        elif (lista[-1] != listacerta[-1]):
            return listacerta[-1]
        i += 1