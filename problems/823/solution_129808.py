def faltante(lista):
    """Retorna o número inteiro da lista que está faltando; lista -> int."""
    n = len(lista) + 1
    x = 1
    i = 0
    list.sort(lista)
    while i < len(lista) and x == lista[i]:
        x = x + 1
        i = i + 1
    return x