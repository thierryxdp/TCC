def maiores(lista,n):
    lista.append(n)
    lista01 = sorted(lista)
    n = lista01.index(n)
    if n not in lista01:
        lista.append(n)
        return lista01[n + 1:]