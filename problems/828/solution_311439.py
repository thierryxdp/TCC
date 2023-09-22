def primo(n):
    '''Verifica se um número n dado é primo ou não
    int -> bool'''
    divisores = []
    for i in range(1, n+1):
        if n%i == 0:
            list.append(divisores,i)
    if len(divisores) > 2:
        return False
    else:
        return True