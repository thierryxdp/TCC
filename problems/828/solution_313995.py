def primo(n):
    contador = []
    for i in range(1,n+1):
        if n%i == 0:
            contador.append([i])
    if len(contador) != 2:
        resultado = False
    else:
        resultado = True
    return resultado