def primo(numero):
    '''Função que retorna se o número é primo ou não, int -> bool'''
    x = 0
    n = 0
    for x in range(2, n + 1):
        if(numero%x == 0):
            return True
        else:
            return False