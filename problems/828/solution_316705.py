def primo(numero):
    '''Recebe um número inteiro positivo e verifica
    se é primo ou não.
    int -> bool'''
    total = 0
    
    for i in range(1,numero + 1):
        if numero % i == 0:
            total += 1
    if total == 2:
        return True
    else:
        return False