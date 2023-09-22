def filtra_pares(tupla):
    '''Função que retorna uma tupla contendo apenas os elementos pares da tupla original de quatro elementos; tuple(int,int,int,int) -> tuple'''
    tuplanova = ()
    testetupla0 = int(tupla[0])%2
    testetupla1 = int(tupla[1])%2
    testetupla2 = int(tupla[2])%2
    testetupla3 = int(tupla[3])%2
    if testetupla0 == 0:
        return tuplanova + (tupla[0],)
    else: 
        return tuplanova 
    and if testetupla1 == 0:
        return tuplanova + (tupla[1],)
    else:
        return tuplanova 
    and if testetupla2 == 0:
        return tuplanova + (tupla[2],)
    else:
        return tuplanova
    and if testetupla3 == 0:
        return tuplanova(tupla[3],)
    else:
        return tuplanova