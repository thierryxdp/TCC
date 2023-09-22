def primo(numero):
    '''verifica se um número inteiro positivo dado é primo ou não
    int -> bool'''
    multiplo = 0
    for contador in range(2,numero):
        if numero % contador == 0:
            multiplo += 1
    if multiplo == 0:
        return True
    else:
        return False