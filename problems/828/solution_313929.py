def primo(n):
    '''
    Função que dado um número positivo, verifica se este
    número é primo ou não.
    
    int -> bool
    '''
    if n % 2 == 0:
        return False
    for a in range(3,n,2):
        if n % a == 0:
            return False
    return True