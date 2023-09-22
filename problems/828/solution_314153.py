def primo(n):
    numeros = []
    for n_elementos in range(1, n + 1):
        if n % n_elementos == 0:
            list.append(numeros, n_elementos)
    if len(numeros) > 2:
        return False
    else:
        return True