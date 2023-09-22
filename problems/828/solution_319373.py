def primo(n):
    '''Dado um número inteiro positivo, verifica se o número é
primo ou não. int-> bool'''
    resultado=0
    for i in range(2,4):
        if n%i==0:
            resultado+=1
    if resultado>0:
        return False
    else:
        return True