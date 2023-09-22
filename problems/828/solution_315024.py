def primo(numero):
    """."""
    y = 0
    for x in range(2, numero):
        if numero%(x) == 0:
            y = 1
        if y == 1:
            return False
        if y == 0:
            return True