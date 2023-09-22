def primo(n):
    for c in range(1, n):
        if n % c == 0:
            print('True')
        else:
            print('False')