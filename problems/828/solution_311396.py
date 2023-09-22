def primo(numero):
    '''Dado um número inteiro positivo, verifica se este número é primo
    int -> boo'''
    for i in range(numero):
        if numero>i>1 and numero%i != 0:
            return True
        else:
            return False