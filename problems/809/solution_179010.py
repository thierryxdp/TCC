def intercala(lista1, lista2) -> lista:
    assert len(lista1) == len(lista2)
    n = len(lista1)
    combined = []
    for i in range(n):
        combined.append(lista1[i])
        combined.append(lista2(lista2[i])