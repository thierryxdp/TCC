def primo(numero):
    '''Diz se o número é primo ou não.
    int -> bool'''
    for i in range(2,numero):
        if numero == 1:
            return False
        if numero == 2:
            return True
        if numero%2==0:
            return False
        if str(numero)[-1] == '0':
            return False
        if str(numero)[-1] == '5':
            return False
        if numero%i == 0:
            return False
    else:
        return True