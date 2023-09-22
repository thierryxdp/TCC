def primo(x):
    """essa função recebe um número e, usando o laço for 
    define se este é primo ou não;
    int->bool"""
    for c in range(2,x):
        if x%c==0:
            return False
    return True