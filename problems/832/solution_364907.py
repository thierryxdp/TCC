def eh_quadrada(matriz):
    '''diz se uma matriz é quadrada (true) ou nao (false)
    list -> bool'''
    contadorL = 0
    contadorC = 0  
    for linha in matriz:
        contadorL = contadorL + 1
        for j in linha:
            contadorC = contadorC + 1      
    if contadorL*contadorL == contadorC:
        return True
    else:
        return False