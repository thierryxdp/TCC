def primo(n):
    """Funcao que recebe um valor n e retorna se eh ou nao primo.Int-->Int"""
    count = 2
    while count <= n:
        if (n%count == 0) and (count == n):
            return True
        elif (n%count == 0) and (count != n):
            return False
        count += 1