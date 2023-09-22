def maiores(lista,n):
    maiores=lista()
    for c in lista:
        if c >= n:
            maiores.append(c)
    return maiores