def faltante(lista):
    tamLista = len(lista) + 1
    pecas = []
    n = 1
    while n < tamLista:
        pecas += [(n + 1),]
        n = n+1
    return n