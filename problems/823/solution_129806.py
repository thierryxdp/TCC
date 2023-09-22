def faltante(lista):
    """Retorna o número inteiro da lista que está faltando; lista -> int."""
    n = len(lista) + 1
    x = n
    i = len(lista)
    list.sort(lista)
    while x == lista[i]:
        x = x - 1
        i = i - 1
    return x