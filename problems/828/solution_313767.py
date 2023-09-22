def primo(n: int) -> bool:
    """função que retorna se o número é primo ou não
    int->bool"""
    if n >= 2:
        for y in range(2, n):
            if not (n % y):
                return False