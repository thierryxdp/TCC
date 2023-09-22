def primo(num):
    '''Função que retorna um valor booleano para um número
    verificando se ele é primo ou não.
    num=int->bool'''
    w = 1
    y = 1
    while w != num:
        if num == 2 or num == 1:
            return True
        elif num%2 == 0 and num!=2:
            return False
        elif num%w == 0:
            y = y + 1
        w = w + 2
    if y > 2:
        return False
    else:
        return True