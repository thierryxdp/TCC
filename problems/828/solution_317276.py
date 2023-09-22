def primo(numero):
    '''
    Função que dada um numero inteiro positivo, verifica se ele é primo ou não, retornando True ou False respectivamente
    int-> booleano
    '''
    mult=0
    for i in range(2,numero):
        if (numero % i == 0):
            mult+=1
    if mult==0:
        return True
    else:
        return False