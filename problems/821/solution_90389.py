def fatorial (n):
    """recebe um numero e calcula o fatorial deste numero."""
    i = n-1
    while i > 0:
        n *= i
        i -= 1
    return n