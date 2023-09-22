def primo(numero):
    """."""
    y = 0
    for x in range(numero-1):
        if numero%x+1 == 0:
            y = y + 1
        if y != 0:
            return False
        if y == 0:
            return True