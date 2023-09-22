def primo(n):
    """Retorna verdadeiro ou falso se o número dado é primo ou não; int -> bool."""
    for i in range(1,n):
        if n%i == 0:
            return False
        else:
            return True