def filtra_pares(tupla):
    '''recebe uma tupla com quatro elementos e retorna os pares
    tupla -> tupla'''
    if tupla[0]%2 == 0:
        return [tupla[0]]
    elif tupla[1]%2 == 0:
        return [tupla[0],tupla[1]]
    elif tupla[2]%2 == 0:
        return [tupla[0],tupla[1], tupla[2]]
    elif tupla[3]%2 ==0:
        return[tupla[0],tupla[1], tupla[2], tupla[3]]