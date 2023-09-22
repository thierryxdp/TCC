def primo(numero):
    '''Função que dado um numero inteiro positivo, verifica se o mesmo
    é primo ou não. int->bool'''
    
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True