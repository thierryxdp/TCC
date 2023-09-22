def primo(num):
    if num > 1:
        i = 2
        while i < num:
            if (num % i) == 0:
                return False
            i = i + 1
    return True