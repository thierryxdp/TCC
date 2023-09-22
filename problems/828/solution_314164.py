def primo(n):
    num = []
    for numeros in range(1, n + 1):
        if n % numeros == 0:
            list.append(num, numeros)
    if len(num) > 2:
        return False
    else:
        return True