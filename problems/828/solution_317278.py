def primo(valor):
    '''
    Função que recebe um valor e retorna True se o mesmo for primo
    ou False, caso contrário.

    int -> bool
    '''

    i = 2
    cont = 0
    
    while i <= (valor-1):
        if valor % i == 0:
            cont += 1
        i += 1

    if cont == 0:
        return True
    else:
        return False