def melhor_volta(matriz):
    """Para saber qual kart deu a melhor volta, digite;
    matriz-> int"""
    resp=(0,100,0)
    for Lin in range(0,6):
        for Col in range(0,10):
             if matriz[Lin][Col]<resp[1]:
                resp=(Lin+1,matriz[Lin][Col],Col+1)
                
    return resp