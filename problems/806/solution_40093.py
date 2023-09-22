def colisao(tupla1, tupla2):
    if (max(tupla1[0],tupla1[2]) >= min(tupla2[0],tupla2[2])) or ( max(tupla1[1],tupla1[3]) >= min(tupla2[1],tupla2[3]) ):
        print("True")
        return True
    else:
        print("False")
        return False