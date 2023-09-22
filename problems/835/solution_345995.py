def melhor_volta(matriz):
    """Para saber qual kart deu a maior volta, digite;
    matriz-> int"""
    resp=(0,100,0)
    for Lin in range(1,6):
        for Col in range(1,10):
             if matriz[Lin][Col]<resp[1]:
                    resp=(Lin+1,matriz[Lin][Col],Col)
    return resp