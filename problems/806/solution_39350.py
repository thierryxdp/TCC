#Start your python function here
def colisao(ret1x1,ret1y1,ret1x2,ret1y2,ret2x1,ret2y1,ret2x2,ret2y2):
    "Função na qual verifica a colisão entre 2 objetos retangulares"
    x1=ret1x1 <= ret2x1 <= ret1x2
    x2=ret1x1 <= ret2x2 <= ret1x2
    y1=ret1y1 <= ret2y1 <= ret1y2
    y2=ret1y1 <= ret2y2 <= ret1y2
    if (x2 and y1) or (x1 and y2) == True:
        return True
    else:
        return False