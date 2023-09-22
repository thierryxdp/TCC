def primo(inteiro):
    '''Dado um número inteiro positivo, verifica se ele
    é primo ou não
    int -> bool'''
    primo = True
    for i in range(2, inteiro):
        if inteiro % i == 0:
            primo = False
    return primo