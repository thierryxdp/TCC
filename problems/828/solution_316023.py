def primo(n):
    '''Função que verifica se um número é primo ou não.
    int -> bool '''
    nPrimos = 0
    for i in range(1, n + 1):
        if n % i == 0:
            nPrimos += 1
    if nPrimos == 2:
        return True
    else:
        return False