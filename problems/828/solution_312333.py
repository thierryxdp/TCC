def primo(n):
    ''' funcao que recebe um numero inteiro 
    positivo e diz se ele é primo ou nao. int-> bool'''
    multiplos=0
    for count in range(2,n):
        if (n % count == 0):
            multiplos += 1
    if(multiplos == 0):
        return True
    else:
        return False