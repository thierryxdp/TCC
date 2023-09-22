def primo(num):
    '''Funcao que recebe um numero inteiro positivo e retorna se ele e primo
ou nao'''
    if num <= 1:
        return False
    elif num == 2:
        return True
        for i range(2,num):
            if num%i==0:
            return False
        return True