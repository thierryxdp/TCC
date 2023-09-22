def primo(nip):
    '''Funcao que, dado um numero inteiro positivo,
    diz se ele Ã© primo ou nao.
    int -> bool'''

    for x in range(2,nip):
        if nip % x ==0:
            return False
    else:
            return True