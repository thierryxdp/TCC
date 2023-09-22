def primo(n):
    resultado = 0
    for c in range(1, n + 1):
        if n % c == 0:
            resultado += 1
    if (resultado == 0):
        print('False')
    else:
        print('True')