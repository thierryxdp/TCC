def filtra_pares(tupla):
    '''Recebe uma tupla com quatro elementos e retorna outra tupla, apenas com os elementos pares da tupla inicial, em mesma ordem.
    tuple ---> tuple'''
    elemento_1 = tupla[0]
    elemento_2 = tupla[1]
    elemento_3 = tupla[2]
    elemento_4 = tupla[3]
    
    if type(elemento_1/2) == int and type(elemento_2/2) == int and type(elemento_3/2) == int and type(elemento_4/2) == int:
        return tupla
    elif type(elemento_1/2) == int and type(elemento_2/2) == int and type(elemento_3/2) == int and type(elemento_4/2) != int:
        return tupla[0:4]
    elif type(elemento_1/2) == int and type(elemento_2/2) == int and type(elemento_3/2) != int and type(elemento_4/2) != int:
        return tupla[0:3]
    elif type(elemento_1/2) == int and type(elemento_2/2) != int and type(elemento_3/2) != int and type(elemento_4/2) != int:
        return tupla[0]