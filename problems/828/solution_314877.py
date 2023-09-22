def primo(n):
    """ A funçao primo, dado um número inteiro positivo, verifica se este número é primo ou não<
    int --> bool """
    for i in range(2,n):
        if n%i == 0:
            return False
    return True