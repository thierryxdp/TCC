def primo(n):
    resultado = 1
    for c in range(4, n + 1):
        if n % c == 0:
            print('False')
        else:
            print('True')