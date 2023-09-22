def primo(n):
    """função que retorna verdadeiro ou falso se um numero é primo ou não
    int -> bool"""
    for numero in range(1,n):
        if n % numero == 0:
            return False
        else:
            return True