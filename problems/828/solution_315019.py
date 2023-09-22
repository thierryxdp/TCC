def primo(numero):
    """."""
    y = 0
    for x in range(1, numero-1):
        if numero%(x) == 0:
            y = y + 1
        if y > 0:
            return False
        if y == 0:
            return True