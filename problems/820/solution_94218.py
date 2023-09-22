def posLetra(string, letra, num):
    """ """
    cont = 0
    posicao = 0
    
    for i in string:
        
        if i == letra:
            if cont == num:
                posicao = cont
            else:
                cont +=1
    return posicao