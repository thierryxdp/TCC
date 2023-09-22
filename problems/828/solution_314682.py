def primo(numero):
    '''Funcao que, dado um numero - inteiro e positivo - de entrada, verifica se ele e primo ou nao; int -> bool'''
    i=0
    while i<numero:
        if numero%i!=0:
            return True
        else:
            return False