def filtra_pares(tupla):
    '''Recebe uma tupla com 4 numeros e retorna os numeros pares na ordem em que se encontram
    tuple -> tuple'''
    pos0 = tupla[0] % 2
    pos1 = tupla[1] % 2
    pos2 = tupla[2] % 2
    pos3 = tupla[3] % 2
    if pos0 == 0 and pos1 == 0 and pos2 == 0 and pos3 == 0:
        return tupla[0], tupla[1], tupla[2], tupla[3]
    elif pos0 == 0 and pos1 == 0 and pos2 == 0 and pos3 == 1:
        return tupla[0], tupla[1], tupla[2]
    elif pos0 == 0 and pos1 == 0 and pos2 == 1 and pos3 == 0:
        return tupla[0], tupla[1], tupla[3]
    elif pos0 == 0 and pos1 == 0 and pos2 == 1 and pos3 == 1:
        return tupla[0], tupla[1]
    elif pos0 == 0 and pos1 == 1 and pos2 == 0 and pos3 == 0:
        return tupla[0], tupla[2], tupla[3]
    elif pos0 == 0 and pos1 == 1 and pos2 == 0 and pos3 == 1:
        return tupla[0], tupla[2]
    elif pos0 == 0 and pos1 == 1 and pos2 == 1 and pos3 == 0:
        return tupla[0], tupla[3]
    elif pos0 == 0 and pos1 == 1 and pos2 == 1 and pos3 == 1:
        return tupla[0],
    elif pos0 == 1 and pos1 == 0 and pos2 == 0 and pos3 == 0:
        return tupla[1], tupla[2], tupla[3]
    elif pos0 == 1 and pos1 == 0 and pos2 == 0 and pos3 == 1:
        return tupla[1], tupla[2]
    elif pos0 == 1 and pos1 == 0 and pos2 == 1 and pos3 == 0:
        return tupla[1], tupla[3]
    elif pos0 == 1 and pos1 == 0 and pos2 == 1 and pos3 == 1:
        return tupla[1],
    elif pos0 == 1 and pos1 == 1 and pos2 == 0 and pos3 == 0:
        return tupla[2], tupla[3]
    elif pos0 == 1 and pos1 == 1 and pos2 == 0 and pos3 == 1:
        return tupla[2],
    elif pos0 == 1 and pos1 == 1 and pos2 == 1 and pos3 == 0:
        return tupla[3],
    elif pos0 == 1 and pos1 == 1 and pos2 == 1 and pos3 == 1:
        return ()