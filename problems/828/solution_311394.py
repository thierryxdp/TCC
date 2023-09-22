def primo(numero):
    '''Dado um número inteiro positivo, verifica se este número é primo
    int -> boo'''
    for i in range(numero):
        if i>1 and numero%i == 0:
            i = i+1
    return False
        else:
    return True