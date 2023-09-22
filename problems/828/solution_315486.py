def primo(numero):
    '''Funçao que dado um numero numero inteiro positivo diz se ele é primo ou nao int-<bool'''
    for x in range(2,numero):
        if numero % x ==0:
            return False
        else:
            return True