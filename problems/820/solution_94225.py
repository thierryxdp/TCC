def posLetra(string, letra, num):
    """ """
    cont = -1
    posicao = 0
    achouLetra = False
    achouLetraNum = False
    while achouLetraNum == False:
        if string[posicao] == letra:
            achouLetra = True
            if posicao == num:
                achouLetraNum = True
                
                
    return posicao