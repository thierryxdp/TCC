def qtd_divisores(n):
    lista = []
    for num in range(n):
        if n % num == 0:
            lista.append(num)
    return len(lista)