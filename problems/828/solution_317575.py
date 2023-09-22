def primo(n):
    '''
    Função que dado um número inteiro positivo, verifica se este é ou não 
    um número primo
    int -> bool
    '''
    if n < 2:
        return False
    else:
        for m in range(2, n):
            if n % m == 0:
                return False
        return True