def primo(numero):
    '''Verifica se o número é primo ou não;
    int -> bool'''
    #Haha. Maybe next time. Vamos do jeito clássico
    if numero == 2:
        return True
    for counter in range(2, numero):
        if numero % counter == 0:
            return True
    return False