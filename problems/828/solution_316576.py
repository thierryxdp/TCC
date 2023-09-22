def primo(n):
    '''A função verificará se um determinado numero (n) é primo ou não.
    Dados de entrada -> int
    Dados de saída -> booleano'''
    
    qtd = qtd_divisores(n)
    
    if qtd != 2:
        return False
    
    else:
        return True