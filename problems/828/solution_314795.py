def primo(n):
    """ Dado um número inteiro positivo, verifica se este número é primo ou não 
    int -> bool """
    for i in range(2, n//2+1):
        if n%i==0:
            return False
    return True