def qtd_divisores(z):
    x = 1
    y = []
    while x < z:
        if z%x == 0:
            y = y + [x]
        x = x + 1
    return len(y)