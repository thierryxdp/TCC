def primo(n):
    """fkldjkfl"""
    i = 0
    for x in range(1, n+1):
        if n % x == 0:
            i += 1
    if i== 2:
        return True
    else:
        return False