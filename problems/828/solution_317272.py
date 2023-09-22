def primo(numero):
    '''
    Função que dada um numero inteiro positivo, verifica se ele é primo ou não, retornando True ou False respectivamente
    int-> booleano
    '''
    if numero>1:
        for i in range(2,numero):
            if (numero%1) == 0:
                return False
            else:
                return True