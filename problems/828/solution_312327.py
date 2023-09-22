def primo(n):
    '''funcao que dado um numero inteiro positivo, diz se eh um numero primo ou nao
    int -> boolean'''
    contador = 1
    for i in range(1, n):
        if ((n % i) == 0):
            contador += 1
    if contador == 2:
        return True
    else:
        return False