def posLetra(string, letra, num):
    """ """
    posicao = 0
    i = 0
    ocorr = 0
    while i < len(string):
        i += 1
        for l in string:
            posicao +=1
            if l == letra:
                ocorr += 1
                if ocorr == num:
                    i = len(string)
    if ocorr < num:
        posicao = -1
    
    return posicao