def primo(inteiro):
    '''recebe um inteiro e retorna True se for primo e False se não for primo
    int -> bool
    '''
    cont = inteiro // 2
    verif = 0
    for i in range(cont):
        i += 1
        if (inteiro %i == 0):
            verif +=  1
    if (verif > 1):
        return False
    else:
        return True