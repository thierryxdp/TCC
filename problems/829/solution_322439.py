def soma_h(n):
    """Calcula a soma H até n
    int --> int"""
    s = 0
    i = 0
    while i <= n:
        s = s + (1/(i+1))
        i = i + 1
    return round(s,2)