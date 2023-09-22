def colisao ():
    tupla1 = (0,0,1,1)
    tupla2 = (2,2,3,3)
    if tupla1[0:2] <= tuple(tupla2[0]) <= tupla1[2:]:
        return True
    if tupla1[0:2] <= tuple(tupla2[1]) <= tupla1[2:]:
        return True
    if tupla1[0:2] <= tuple(tupla2[2]) <= tupla1[2:]:
        return True
    if tupla1[0:2] <= tuple(tupla2[3]) <= tupla1[2:]:
        return True
    if tupla2[0:2] == tupla1[0:2]:
        return True
    if tupla2[0:] <= tupla1[0:1]:
        return True
    else:
        return False