def primo(num):
    '''Verifica se o numero é primo e retorna true para sim e false para nao
    int--->bool'''
    soma = 0
    for n in range(num, 0, -1):
        if num % n == 0:
            soma += 1
    if soma <= 2:
        return True
    else:
        return False