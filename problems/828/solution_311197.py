def primo(n):
    '''
    Verifica se um numero e primo ou nao
    
    Entrada/Saida:
    int -> bool
    '''
    for i in range(2, n):
        if not (n % i):
            return False
    return True