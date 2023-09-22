def primo(numero):
    '''
    Função que dada um numero inteiro positivo, verifica se ele é primo ou não, retornando True ou False respectivamente
    int-> booleano
    '''
    for i in range(numero):
        if numero % i != 0:
            return True
        else:
            return False