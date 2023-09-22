def primo(numero):
    '''Função que retorna se o número é primo ou não, int -> bool'''
    x = 0  
    n = 2
    for x in range(2, n + 1):
        if(n%x == 0):
            x = x + 1
            return False
        if(x <= 2):
            return True