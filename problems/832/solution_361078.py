def eh_quadrada(matriz):
    nlin = len(matriz)
     
    if nlin == 0:
        return True
    elif nlin == len(matriz[0]) :
        return True
    elif nlin != len(matriz[0]):
        return False