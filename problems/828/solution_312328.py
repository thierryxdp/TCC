def primo(n):
    '''funcao que dado um numero inteiro positivo, diz se eh um numero primo ou nao
    int -> boolean'''
    contador = 1
    metade = n//2
    for i in range(1, metade + 1):
        if ((n % i) == 0):
            contador += 1
    if contador == 2:
        return True
    else:
        return False