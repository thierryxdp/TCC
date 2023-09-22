def primo(n):
    '''funcao que dado um numero inteiro diz se é primo ou não'''
    contador = 1
    metade = n//2
    for i in range (1, metade+1):
        if((n % i) == 0):
            contador += 1
    if contador == 2:
        return True
    else:
        return False