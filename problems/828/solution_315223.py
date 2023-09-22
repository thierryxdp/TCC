def primo(n):
    """
    Retorna se o número é primo ou não.
    int -> bool
    """
    div=0
    for i in range(1,n):
        if n%i==0:
            div += 1
    if div > 1:
        return False
    else:
        return True