def primo(n):
    """função que retorna verdadeiro ou falso se um numero é primo ou não
    int -> bool"""
    for numero in range(1,n-1):
        if (n%numero==0):
            return True
        else:
            return False