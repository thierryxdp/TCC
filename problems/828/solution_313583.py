def primo(n):
    lista = []
    numero = list(range(n))
    for x in numero:
        if x % n == 0:
            list.append(lista, x)
    return len(lista) == 0