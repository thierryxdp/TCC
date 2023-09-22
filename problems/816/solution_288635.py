def maiores(lista,n):
    lista.append(n)
    lista01 = sorted(lista)
    N = lista01.index(n)
    if n not in lista01:
        lista.append(n)
        return lista01[N + 1:]