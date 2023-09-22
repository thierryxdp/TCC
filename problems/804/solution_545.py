def filtra_pares(tupla):
    '''Função que retorna uma tupla contendo apenas os elementos pares da tupla original de quatro elementos; tuple(int,int,int,int) -> tuple'''
    tuplanova = ()
    if int(tupla[0])%2 == 0:
        return tuplanova2 = tuplanova + (tupla[0],)
    else: 
        return tuplanova2 = tuplanova
    if int(tupla[1])%2 == 0:
        return tuplanova3 = tuplanova2 + (tupla[1],)
    else:
        return tuplanova3 = tuplanova2 
    if int(tupla[2])%2 == 0:
        return tuplanova4 = tuplanova3 + (tupla[2],)
    else:
        return tuplanova4 = tuplanova3
    if int(tupla[3])%2 == 0:
        return tuplanova5 = tuplanova4 + (tupla[3],)
    else:
        return tuplanova5 = tuplanova4
    return: tuplanova5