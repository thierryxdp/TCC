def primo(n):
    """função que retorna verdadeiro ou falso se um numero é primo ou não
    int -> bool"""
    for count in range(2,n):
        if (n % count == 0):
            return True
        else:
            return False