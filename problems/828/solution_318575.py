def primo(numero):
    '''função que dado um numero inteiro positivo, verifica se ele
    é primo ou não. retornando um valor booleano;
    int-> bool'''
    for i in range(2,numero):
        if numero % i ==0:
            return False
    return True