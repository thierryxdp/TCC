def posLetra(string, letra, num):
    """ """
    cont = -1
    posicao = 0
    achouLetra = False
    achouLetraNum = False
    i = 0
    s = ""
    ocorr = 0
    while i < len(string):
        i += 1
        for l in string:
            if l == letra:
                achouLetra = True
                ocorr += 1
                if ocorr == num:
                    achouLetraNum = True
                else:
                    ocorr +=1
                    posicao += 1
    if achouLetraNum == False:
        posicao = -1
    
    return posicao