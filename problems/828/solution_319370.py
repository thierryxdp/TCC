def primo(n):
    '''Dado um número inteiro positivo, verifica se o número é
primo ou não. int-> bool'''
    resultado=0
    for i in range(1,4):
        if n%i==0:
            resultado+=1
    if resultado>1:
        return True
    else:
        return False