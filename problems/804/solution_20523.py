def filtra_pares(n1, n2, n3, n4):
    '''função que retorna um conjunto com os números pares contidos nas entradas; int, int ,int, int -> tupla'''
    resto1 = (n1) % 2
    resto2 = (n2) % 2
    resto3 = (n3) % 2
    resto4 = (n4) % 2
    if resto1 == 0 and resto2 == 0 and resto3 == 0 and resto4 == 0:
        return (n1, n2, n3, n4)
    elif resto1 == 0 and resto2 == 0 and resto3 == 0:
        return (n1, n2, n3)
    elif resto1 == 0 and resto2 == 0 and resto4 == 0:
        return(n1, n2, n4)
    elif resto1 == 0 and resto3 == 0 and resto4 == 0:
        return (n1, n3, n4)
    elif resto2 == 0 and resto3 == 0 and resto4 == 0:
        return (n2, n3, n4)
    elif resto1 == 0 and resto2 == 0:
        return (n1, n2)
    elif resto2 == 0 and resto3 == 0:
        return(n2, n3)
    elif resto2 == 0 and resto4 == 0:
        return (n2, n4)
    elif resto1 == 0 and resto3 == 0:
        return (n1, n3)
    elif resto1 == 0:
        return (n1,)
    elif resto2 == 0:
        return (n2,)
    elif resto3 == 0:
        return (n3,)
    elif resto4 == 0:
        return (n4,)
    else:
        return ()