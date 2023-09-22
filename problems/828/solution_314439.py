def primo(num):
    for foda in range(num):
        if foda > 1:
            if num % foda == 0:
                return False
    return True