def primo(numero):
    '''esta função verifica se um número quelquer é primo
    int --> bool'''
    cnt = 0
    for elemento in range(2,numero):
        if numero % elemento == 0:
            cnt += 1
    if cnt > 0:
        return False
    else:
        return True