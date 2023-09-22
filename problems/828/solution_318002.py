def primo(n):
    if n != 0 and n != 1:
        if n > 3:
            for i in range(2, n):
                if n % i == 0:
                    return False
        return True
    return False