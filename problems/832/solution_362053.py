def eh_quadrada(matriz):
    """retorna o fato de a mmatriz ser ou nao quadrada"""
    linha=len(matriz)
    a=[]
    if a==matriz:
        return 'True'
    else:
        coluna=len(matriz[0])
    if linha==coluna:
        return 'True'
    else:
        return 'False'