def posLetra(string, letra, num):
    """ """
    cont = -1
    posicao = 0
    achouLetra = False
    achouLetraNum = False
    i = 0
    s = ""
    ocorr = -1
    
    for l in string:
        
        if l == letra:
            
            achouLetra = True
            
            if ocorr == num:
                achouLetraNum = True
            else:
                ocorr +=1
        else:
            posicao += 1
    if achouLetraNum != True:
        posicao = -1
    return posicao