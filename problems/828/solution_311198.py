def primo(n):
    '''Essa função verifica se o inteiro inserido é um número primo ou
    não, retornando True se sim e False se não;
    INT -> BOOL'''
    for i in range(2, n):
        if (n%i) == 0:
            return False
        else:
            return True