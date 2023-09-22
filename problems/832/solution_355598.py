def eh_quadrada(matriz):
    linham =len(matriz)
    colunam =len(matriz[0])
    quadrada =True
    if linham ==colunam:
        return quadrada
    else:
        return not quadrada