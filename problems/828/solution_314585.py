def primo(numero):
    '''retorna se o número é primo ou não.
    int -> bool'''
    for i in range(1,numero+1):
        if i // numero:
            return False
        else:
            return True