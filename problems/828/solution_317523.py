def primo(numero):
    '''verifica se um número inteiro positivo dado é primo ou não
    int -> bool'''
    multiplo = 0
    for contador in range(2,n):
        if n % contador == 0:
            multiplo += 1
    if multiplo == 0:
        return True
    else:
        return False