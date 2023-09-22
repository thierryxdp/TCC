def primo(num):
    '''Dado um número inteiro, retorna dizendo se ele é primo ou não.
    int -> bol'''
    divisores = 0
    i = 1
    for i in range(1, num + 1):
        if num % i == 0 :
            divisores = divisores + 1
        i = i + 1
    if divisores == 2:
        return True
    else:
        return False