def filtra_pares(s):
    '''Dados 4 valores, filtra apenas os valores pares inseridos
    na mesma ordem de inserção;
    tup->tup'''
    s2=()
    if s[0] % 2 == 0:
        return s2 + (s[0],)
    elif s[1] % 2 == 0:
        return s2 + (s[1],)
    elif s[2] % 2 == 0:
        return s2 + (s[2],)
    elif s[3] % 2 == 0:
        return s2 + (s[3],)
    else:
        return s2