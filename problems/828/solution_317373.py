def primo(numero):
    '''retorna se o numero é primo
    int -> bool'''
    j = 0
    for i in range(1, numero+1):
        if numero%i ==0:
            j += 1
    if j == 2:
        return True
    else:
        return False