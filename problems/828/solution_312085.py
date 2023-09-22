def primo(n):
    num = n

    for c in range(1,num + 1):
        if num % c == 0:
            return True
        else:
            return False