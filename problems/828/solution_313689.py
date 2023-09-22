def primo(num):
    '''Função que retorna um valor booleano para um número
    verificando se ele é primo ou não.
    num=int->bool'''
    proximo = 1
    counter = 1
    while proximo != num:
        if num == 2 or num == 1:
            return True
        elif num%2 == 0 and num!=2:
            return False
        elif num%proximo == 0:
            counter = counter + 1
        proximo = proximo + 2
    if counter > 2:
        return False
    else:
        return True