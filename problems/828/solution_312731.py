def primo(n):
    if n <= 0:
        return 'O numero n precisa ser positivo'
    else:
        for index in range(2, n):
            if n%index == 0:
                return False
            elif n%index != 0:
                return True