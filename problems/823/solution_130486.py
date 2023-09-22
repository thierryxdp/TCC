def faltante(lista):
    N = len(lista)
    total = (N + 1)*(N + 2)//2
    listaint = sum(lista)
    return total - listaint