def primo(n):
    """Verifica se o n numero é primo ou não, retornando um valor booleano True ou False
    n --> in, n >= 0
    contador --> lista
    resultado --> booleano
    """
    contador = []
    for i in range(1,n+1):
        if n%i == 0:
            contador.append([i])
    if len(contador) != 2:
        resultado = False
    else:
        resultado = True
    return resultado