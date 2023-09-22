def primo(numero):
    if numero == 2 or numero == 3:
            return True
    for x in range(2,(numero//2)+1):
        if numero%x == 0:
            return False
        else:
            return True