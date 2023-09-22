def primo(n):
    '''Dado um número inteiro positivo, verifica se o número é
primo ou não. int-> bool'''
    resultado=0
    for i in range(2,n):
        if n%i==0:
            return False
    return True