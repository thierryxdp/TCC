def colisao(ret1, ret2):
    '''
    Entrada:
        É fornecido as condenadas(int) dos vértices sup e inf de cada retangulo ---> tuple
    Saída:
        Retorna se eles estão em contato ---> bool
    '''

    xi1= int(ret1[0])
    yi1= int(ret1[1])
    xs1= int(ret1[2])
    ys1= int(ret1[3])

    xi2= int(ret2[0])
    yi2= int(ret2[1])
    xs2= int(ret2[2])
    ys2= int(ret2[3])

    if (xs1-xi2) >= 0 and (ys1-yi2) >= 0 and (xs2-xi1) >= 0 and (ys2-yi1) >= 0:
        return True

    else:
        return False