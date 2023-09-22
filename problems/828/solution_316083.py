def primo(numero):
    '''Função que ao receber um número inteiro positivo verifica se ele é
primo.'''
    #int -> bool
    divisores = 0
    for n in range(1, numero + 1):
        if numero % n == 0:
            divisores += 1
    if divisores == 2:
        return True
    else:
        return False