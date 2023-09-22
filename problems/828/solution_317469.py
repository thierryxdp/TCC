def primo(Num):
    '''Função que dado um número inteiro positivo, verifica se este número é primo ou não.
    int -> bool'''
    divisores = 0
    for c in range(1, Num + 1):
        if Num % c == 0:
            divisores = divisores + 1
    if divisores == 2:
        return True
    else:
        return False