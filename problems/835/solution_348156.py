def melhor_volta(matriz):
    """Função que receba uma matriz 6x10 e retorna uma tupla; list-> tuple"""
    t=(0,float(),0)
    for i in range(len(6)):
        for j in range(len(10)):
            if matriz[i][j]<t[1]:
                t=(i+1,matriz[i][j],j+1)
    return t