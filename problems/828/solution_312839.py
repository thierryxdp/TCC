def primo(n):
    lista = []
    for num in range(1, n + 1):
        if n % num == 0:
            lista.append(num)
    if len(lista) > 2:
        return False
    elif len(lista) < 2:
        return True