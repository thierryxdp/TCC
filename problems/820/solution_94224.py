def posLetra(string, letra, num):
    """ """
    cont = -1
    posicao = 0
    achou = False
    for i in string:
        if i == letra:
            achou = True
            if cont == num:
                posicao = cont
            else:
                achou = False
    if achou == True:
        if cont < num:
            posicao = cont
        else:
            if cont == num:
                posicao = cont
    return posicao