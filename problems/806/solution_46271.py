def colisao():
    tupla1 = (a,b,c,d)
    tupla2 = (a,b,c,d)
    if tupla2[0:2] == tupla1[0:2]:
        return True
    if tupla2[0:] <= tupla1[0:]:
        return True
    else:
        return False