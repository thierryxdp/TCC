def primo(x):
    '''Função que dado um número primo inteiro positivo, verifica se este número é primo ou não; int -> bool'''
    if x >= 2:
        for y in range(2, x):
            if not ( x % y):
                return False
    else:
        return False