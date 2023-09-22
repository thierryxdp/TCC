def filtra_pares(tupla):
    '''Recebe uma tupla com quatro elementos e retorna outra tupla, apenas com os elementos pares da tupla inicial, em mesma ordem.
    tuple ---> tuple'''
    elemento_1 = tupla[0]
    elemento_2 = tupla[1]
    elemento_3 = tupla[2]
    elemento_4 = tupla[3]
    if elemento_1%2 == 0 and elemento_2%2 == 0 and elemento_3%2 == 0 and elemento_4%2 == 0:
        return tuple([tupla])
    elif elemento_1%2 == 0 and elemento_2%2 == 0 and elemento_3%2 == 0 and elemento_4%2 != 0: 
        return tuple([tupla[0:3]])
    elif elemento_1%2 == 0 and elemento_2%2 == 0 and elemento_3%2 != 0 and elemento_4%2 != 0: 
        return tuple([tupla[0:2]])
    elif elemento_1%2 == 0 and elemento_2%2 != 0 and elemento_3%2 != 0 and elemento_4%2 != 0: 
        return tuple([tupla[0]])
    elif elemento_1%2 != 0 and elemento_2%2 != 0 and elemento_3%2 != 0 and elemento_4%2 != 0:
        return ()
    elif elemento_1%2 == 0 and elemento_2%2 != 0 and elemento_3%2 == 0 and elemento_4%2 != 0: 
        return tuple([tupla[0]]) + tuple([tupla[2]])
    elif elemento_1%2 == 0 and elemento_2%2 != 0 and elemento_3%2 != 0 and elemento_4%2 == 0: 
        return tuple([tupla[0]]) + tuple([tupla[-1]])
    elif elemento_1%2 != 0 and elemento_2%2 == 0 and elemento_3%2 == 0 and elemento_4%2 != 0: 
        return tuple([tupla[1]]) + tuple([tupla[2]])
    elif elemento_1%2 != 0 and elemento_2%2 == 0 and elemento_3%2 != 0 and elemento_4%2 != 0: 
        return tuple([tupla[1]]) + tuple([tupla[-1]])
    elif elemento_1%2 != 0 and elemento_2%2 == 0 and elemento_3%2 != 0 and elemento_4%2 != 0:
        return tuple([tupla[1]])
    elif elemento_1%2 != 0 and elemento_2%2 != 0 and elemento_3%2 == 0 and elemento_4%2 != 0: 
        return tuple([tupla[-2]])
    elif elemento_1%2 != 0 and elemento_2%2 != 0 and elemento_3%2 != 0 and elemento_4%2 == 0: 
        return tuple([tupla[3]])
    elif elemento_1%2 != 0 and elemento_2%2 != 0 and elemento_3%2 == 0 and elemento_4%2 == 0:
        return tuple([tupla[2]]) + tuple([tupla[-1]])
    elif elemento_1%2 == 0 and elemento_2%2 == 0 and elemento_3%2 != 0 and elemento_4%2 == 0: 
        return tuple([tupla[0:2]]) + tuple([tupla[-1]])
    elif elemento_1%2 == 0 and elemento_2%2 != 0 and elemento_3%2 == 0 and elemento_4%2 == 0: 
        return tuple([tupla[0]]) + tuple([tupla[-2:]])
    elif elemento_1%2 != 0 and elemento_2%2 == 0 and elemento_3%2 == 0 and elemento_4%2 == 0: 
        return tuple([tupla[1:]])