def eh_quadrada(matriz):
    '''Função que identifica se uma matriz é quadrada;
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