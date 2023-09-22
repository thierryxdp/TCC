def primo(n):
    """função que retorna verdadeiro ou falso se um numero é primo ou não
    int -> bool"""
    multiplos=0
    for numero in range(2,n):
        if (n % numero == 0):
            return False
    else (n % numero != 0):
        return True