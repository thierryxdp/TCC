def maiores(lista, n):

    i=0
    while i <= n:
        i=i+1
        if i > n:
            lista = list(lista) + lista[i]
            return lista