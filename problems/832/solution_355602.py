def eh_quadrada(matriz):
    '''recebe uma matriz e retorna se ela é quadrada.
    list ->bool'''
    linham =len(matriz)
    colunam =len(matriz[0])
    quadrada =True
    if linham ==0 and colunam ==0:
        return quadrada
    if linham ==colunam:
        return quadrada
    else:
        return not quadrada