def primo(numero):
    '''Funcao que, dado um numero de entrada (numero), retorna se ele é primo ou nao; int -> bool'''
    for div in range(2,round(numero/2)+1):
        if numero%div==0:
            return False
        else:
            return True