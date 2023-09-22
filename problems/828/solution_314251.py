def primo(n):
    ''''''
    acumulador = 0
    for i in range(1,n+1):
        if n % i == 0:
            acumulador = acumulador + 1
    if acumulador == 2:
        return True
    else:
        return False