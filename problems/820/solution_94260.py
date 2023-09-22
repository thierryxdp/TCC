def posLetra(string, letra, num):
    """ """
    posicao = 0
    i = 0
    ocorr = 0
    
    for l in string:
        if l == letra:
            ocorr += 1
            if ocorr == num:
                    break
            else:
                posicao += 1
        else:
            posicao += 1
    if ocorr < num:
        posicao = -1
    
    return posicao