def qtd_divisores(n):
    i =1
    lista_de_divisores = []
    while i <= n:
        if n % i == 0:
            lista_de_divisores.append(i)
        i += 1
    return lista_de_divisores