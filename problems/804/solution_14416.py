def filtra_pares(sequencia):
    '''Função que retorna uma tupla apenas com pares da 
    sequencia inserida na tupla original.
    tupla(int, int, int, int) -> tupla(???)'''
    P0 = sequencia[0]
    P1 = sequencia[1]
    P2 = sequencia[2]
    P3 = sequencia[3]
    if P0%2 == 0 and P1%2 == 0 and P2%2 == 0 and P3%2 == 0:
        return (P0,P1,P2,P3)
    elif P0%2 == 0 and P1%2 == 0 and P2%2 == 0:
        return (P0,P1,P2)
    elif P0%2 == 0 and P1%2 == 0 and P3%2 == 0:
        return (P0,P1,P3)
    elif P0%2 == 0 and P2%2 == 0 and P3%2 == 0:
        return (P0,P2,P3)
    elif P1%2 == 0 and P2%2 == 0 and P3%2 == 0:
        return (P1,P2,P3)
    elif P0%2 == 0 and P1%2 == 0:
        return (P0,P1)
    elif P0%2 == 0 and P2%2 == 0:
        return (P0,P2)
    elif P0%2 == 0 and P3%2 == 0:
        return (P0,P3)
    elif P1%2 == 0 and P2%2 == 0:
        return (P1,P2)
    elif P1%2 == 0 and P3%2 == 0:
        return (P1,P3)
    elif P2%2 == 0 and P3%2 == 0:
        return (P2,P3)
    elif P0%2 == 0:
        return (P0,)
    elif P1%2 == 0:
        return (P1,)
    elif P2%2 == 0:
        return (P2,)
    elif P3%2 == 0:
        return (P3,)
    else:
        return ()