def primo(numero):
    '''Função que retorna se o número é primo ou não, int -> bool'''
    x = 0
    n = 0
    for x in range(3, n + 1):
        if(numero%x == 0):
            return True
        for x in range(3, n):
            if(numero%x != 0):
                numero = numero + 1
    return False