def qtd_divisores(n):
    lista = []

    for i in range(n + 1)[1:]:
        if n % i == 0:
            lista.append(i)

    return lista