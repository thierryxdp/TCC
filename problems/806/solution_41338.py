#Start your python function here
def colisao(tupla1, tupla2):
    if (tupla1[0] <= tupla2[0] <= tupla1[2]) and (tupla1[1] <= tupla2[1] <= tupla1[3]):
        return True

    elif (tupla1[0] <= tupla2[2] <= tupla1[2]) and (tupla1[1] <= tupla2[3] <= tupla1[3]):
        return True

    elif (tupla1[0] <= tupla2[0] <= tupla1[2]) and (tupla1[1] <= tupla2[2] <= tupla1[3]):
        return True

    elif (tupla1[0] <= tupla2[2] <= tupla1[2]) and (tupla1[1] <= tupla2[1] <= tupla1[3]):
        return True

    else:
        return False