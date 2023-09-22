def primo(numero):
    '''Função que retorna se o número é primo ou não, int -> bool'''
    x = 0
    for x in range(2, n + 1):
        if(numero%x == 0):
            return True
        for x in range(2, n):
            if(numero%x != 0):
                numero = numero + 1
    return False