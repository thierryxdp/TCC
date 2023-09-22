def posLetra(string, letra, num):
    """ """
    cont = -1
    posicao = -1
    achouLetra = False
    achouLetraNum = False
    i = 0
    s = ""
    ocorr = 0
    while achouLetraNum == False:
        for l in string:
            if l == letra:
                achouLetra = True
                ocorr += 1
                if ocorr == num:
                    achouLetraNum = True
                    posicao += 1
                else:
                    ocorr +=1
     if achouLetraNum == False:
        posicao = -1
    
    return posicao