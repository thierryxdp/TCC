def maiores(lista,n):
    maiores = list()
    list.sort(maiores)
    for c in lista:
    if c >= n:
    maiores.append(c)
        return maiores