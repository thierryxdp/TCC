def primo(n):
    """
    Verifica se o numero é primo
    """
    total=0
    for i in range(1,n+1):
        if n//i==n/i:
            total+=1
    if total>2:
        return False
    else:
        return True