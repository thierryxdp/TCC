def primo (n):
    mult = 0
    for numeros in range (2, n):
        if (n % numeros == 0):
            return (True)
        else:
            return (False)