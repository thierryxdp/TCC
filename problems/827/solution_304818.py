def qtd_divisores(n):
    lista = []
    for num in range(1, n + 1):
        if n % num == 0:
            lista.append(num)
    return len(lista)