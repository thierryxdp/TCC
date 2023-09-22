def posLetra(string, letra, num):
    """ """
    cont = -1
    posicao = 0
    achou = false
    
    for i in string:
        
        if i == letra:
            achou = true
            if cont == num:
                posicao = cont
            else:
                cont +=1
     if achou == true:
        if cont < num:
            posicao = cont
    return posicao