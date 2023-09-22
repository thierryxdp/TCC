def primo(numero):
    '''Define se um número é ou não primo.
    int -> bool'''

    lista = range(2,numero)

    for n in lista:
        if numero//n == numero/n:
            return False

    return True