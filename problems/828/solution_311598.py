def primo (n):
    mult = 0
    for numeros in range (2, n):
        if (n % numeros == 0):
            mult += 1
    if (mult == 0):
        return (True)
    else:
        return (False)