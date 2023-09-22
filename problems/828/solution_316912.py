def primo(n):
    """Funçao que dado o número n, retorna se é um número primo ou não """
    if n==2:
        return True
    for count in range (3, n+1):
        if n% count == 0:
            return count
        mult += 1
    if mult ==0:
        return True
    else:
        return False