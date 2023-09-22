def posLetra(string, letra, num):
    """ """
    cont = -1
    posicao = 0
    achouLetra = False
    achouLetraNum = False
    i = 0
    s = ""
    while achouLetraNum == False:
        l = string[i]
        if l == letra:
            achouLetra = True
            if i == num:
                achouLetraNum = True
            else:
                i +=1
    return i