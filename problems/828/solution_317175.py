def primo(numero):
    '''Função que retorna se o número é primo ou não, int -> bool'''
    x = 2
    n = 0
    for x in range(2, n):
        if(numero%x == 0):
            return True
    return False