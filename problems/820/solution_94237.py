def posLetra(string, letra, num):
    """ """
    cont = -1
    posicao = 0
    achouLetra = False
    achouLetraNum = False
    i = 0
    s = ""
    while achouLetraNum == False:
        for i in string:
            if i == letra:
                achouLetra = True
            if posicao == num:
                achouLetraNum = True
            else:
                posicao +=1
    return posicao