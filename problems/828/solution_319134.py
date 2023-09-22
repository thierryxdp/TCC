def primo(x):
    '''função que verifica se um número inteiro x dado é primo.
    int -> bool'''
    if x < 2:
        return False
    else:
        for i in range(2, x):
            if x%i != 0:
                return True
            else:
                return False