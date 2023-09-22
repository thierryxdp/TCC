def colisao(ret1, ret2):
    """
    Função que detecta se dois quadrados, em um plano cartesiano, estão sobrepostos.
    Entrada: ret1 = (X1, Y1, X2, Y2), sendo X1, Y1 as coordenadas de uma das extremidades do retângulo, enquanto X2, Y2 são as coordanadas da extremidade oposta do retângulo
    tupla, tupla -> Boolean
    """

    #Limpar os dados
    X1R1 = ret1[0]
    Y1R1 = ret1[1]
    X2R1 = ret1[2]
    Y2R1 = ret1[3]

    X1R2 = ret2[0]
    Y1R2 = ret2[1]
    X2R2 = ret2[2]
    Y2R2 = ret2[3]




    #Se X1 do R1 estiver entre os X do R2 e o Y1 estiver entre os Y do R2, essa coordenada tá dentro da outra 
    if ((X1R1 >= X1R2) and (X1R1 <= X2R2)) and ((Y1R1 >= Y1R2) and (Y1R1 <= Y2R2)):
        return True

    #Se X2 do R1 estiver entre os X do R2 e o Y2 estiver entre os Y do R2, essa coordenada tá dentro da outra 
    elif ((X2R1 >= X1R2) and (X2R1 <= X2R2)) and ((Y2R1 >= Y1R2) and (Y2R1 <= Y2R2)):
        return True
    
    #Se ninguém partir de dentro de ninguém, tá safe.
    else:
        return False