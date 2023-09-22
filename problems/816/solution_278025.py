def maiores(lista,n):
    x = lista + [n]
    y = list.sort(x)
    return y[:] - y[0:n]