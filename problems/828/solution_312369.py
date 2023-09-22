def primo(n):
    """ Avalia se o numero dado na entrada é primo ou não,
    True pra quando ele é primo e False pra quando não é"""
    """ int -> bool"""
    if n%2 == 0:
        return False
    for numero in range(3,n,2):
        if n%numero == 0:
            return False
    return True