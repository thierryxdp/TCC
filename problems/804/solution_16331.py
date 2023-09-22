def colisao (tupla1, tupla2):
    #tupla1 = (0,0,1,1)
    #tupla2 = (2,2,3,3)
    if tupla1[0:2] <= tupla2[0:2] <= tupla1[2:]:
        return True
    else:
        return False