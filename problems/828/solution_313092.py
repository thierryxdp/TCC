def primo(n):
    """retorna se o numero dado como entrada é primo ou não.
    int->bool"""
    for num in range(2,n):
        if n%num==0:
            return False
    return True