def primo(n):
    """ retorna um valor booleano caso o
    numero passado como parametro seja primo.
    int -> bool"""
    for i in range(2,n):
        if n % i == 0:
            return False
    return True