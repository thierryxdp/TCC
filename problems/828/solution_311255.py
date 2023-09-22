def primo(numero):
    '''Função que dado um numero inteiro positivo verifica se o numero é primo ou não retornando um valor boleano.
    	int -> bool'''

    divisores = 0

    for a in range(1, numero):
        if numero % a == 0:
            divisores += 1
        if divisores > 1:
            break
    if divisores > 1:
        return False
    	else:
        return True