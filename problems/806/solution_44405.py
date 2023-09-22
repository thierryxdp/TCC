def colisao(ret1, ret2):
    """
    Função que detecta se dois quadrados, em um plano cartesiano, estão sobrepostos.
    Entrada: ret1 = (X1, Y1, X2, Y2), sendo X1, Y1 as coordenadas de uma das extremidades do retângulo, enquanto X2, Y2 são as coordanadas da extremidade oposta do retângulo
    tupla, tupla -> Bool
    """

    SemContatoX = ret2[0] > ret1[2] or ret2[2] < ret1[0]
    SemContatoY = ret2[1] > ret1[3] or ret2[3] < ret1[1]

    if SemContatoX and SemContatoY == True:
        return False
    else:
        return True

    #Casos testes: colisao((0,7,15,26), (-10,28,-1, 55)) -> False
    #Casos testes: colisao((4,3,6,6), (6,7,7,8)) -> True