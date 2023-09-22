def colisao(ret1,ret2):
    """Funcao calcula se ocorre colisao entre dois retangulos, retornando
    True quando ocorre e False quando nao ocorre, dadas as coordenadas do
    retangulo no formato de tuplas: ret1(x1,y1,x2,y2) e ret2(x3,y3,x4,y4) """
    
    x1, y1, x2, y2 = ret1
    
    x3, y3, x4, y4 = ret2

    if x3 >= x1 and y3 >= y1 and x3 <= x2 and y3 <= y2:
        return True
    elif x4 >= x1 and y4 >= y1 and x4 <= x2 and y4 <= y2:
        return True
    elif x3 >= x1 and y4 >= y1 and x3 <= x2 and y4 <= y2:
        return True
    elif x4 >= x1 and y3 >= y1 and x4 <= x2 and y3 <= y2:
        return True
    else:
        return False