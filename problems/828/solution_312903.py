def primo(n):
    for c in range(4, n + 1):
        if n % c == 0:
            print('True')
        else:
            print('False')