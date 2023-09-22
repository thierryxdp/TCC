def primo(numero):
    '''dado um numero, verifica se ele e primo retornando true ou false; int -> bool'''
    i = 2
    divisores = []
    while i <= numero:
        if numero%i == 0:
            divisores = divisores + [i,]
        i = i + 1
    if len(divisores) == 1:
        return True
    else:
        return False