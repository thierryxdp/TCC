def primo(num):
    """funcao que diz se um numero e primo ou nao"""
    """int->bool"""
    a = 0
    for a in range(1,num):
        if num % a == 0:
            return False
    return True