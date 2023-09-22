def primo(numero):
    '''
    	Funcao que recebe um numero inteiro positivo e verifica
        se este numero e primo ou nao
        int -> bool
    '''
    divisores = 0
    for i in range(1, numero+1):
    	if numero%i == 0:
            divisores += 1
    if divisores > 0:
        return False
    else:
        return True