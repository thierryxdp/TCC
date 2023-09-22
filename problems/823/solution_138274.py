def faltante(L):
    """Função que dada uma lista com N - 1 inteiros numerados
    de 1 a N, retorna qual número inteiro deste intervalo
    está faltando;
    list -> int"""
    list.sort(L)
    k = -1
    final = len(L) + 1
    comeco = L[0]
    while abs(k) < len(L):
        if L[k] == final:
            final = final - 1
        k = k - 1
    if L[k] != final:
        return final
    elif L[0] == 2:
        return 1