def primo(num):
    '''Função que recebe um numero inteiro positivo,
    verifica se ele é primo ou não e retorna um booleano.
    int -> bool
    '''
    n = 0
    for elemento in range(2,num):
        if num % elemento == 0:
            n += 1

    if n > 0:
        return False
    else:
        return True